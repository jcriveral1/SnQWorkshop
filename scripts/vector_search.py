#!/usr/bin/env python3
import os
import socket
import ssl
import struct
from urllib.parse import urlparse


QUERIES = {
    "fraude": [1.0, 0.0, 0.0, 0.0],
    "credito": [0.0, 1.0, 0.0, 0.0],
    "inversion": [0.0, 0.0, 1.0, 0.0],
    "sucursal": [0.0, 0.0, 0.0, 1.0],
}


def encode_command(parts):
    payload = [f"*{len(parts)}\r\n".encode()]
    for part in parts:
        if isinstance(part, str):
            part = part.encode()
        payload.append(f"${len(part)}\r\n".encode())
        payload.append(part)
        payload.append(b"\r\n")
    return b"".join(payload)


def read_line(sock):
    data = bytearray()
    while not data.endswith(b"\r\n"):
        chunk = sock.recv(1)
        if not chunk:
            raise ConnectionError("Connection closed")
        data.extend(chunk)
    return bytes(data[:-2])


def read_resp(sock):
    prefix = sock.recv(1)
    if prefix == b"+":
        return read_line(sock).decode()
    if prefix == b"-":
        raise RuntimeError(read_line(sock).decode())
    if prefix == b":":
        return int(read_line(sock))
    if prefix == b"$":
        size = int(read_line(sock))
        if size == -1:
            return None
        data = b""
        while len(data) < size:
            data += sock.recv(size - len(data))
        sock.recv(2)
        try:
            return data.decode()
        except UnicodeDecodeError:
            return data
    if prefix == b"*":
        count = int(read_line(sock))
        if count == -1:
            return None
        return [read_resp(sock) for _ in range(count)]
    raise RuntimeError(f"Unknown RESP prefix: {prefix!r}")


def command(sock, *parts):
    sock.sendall(encode_command(parts))
    return read_resp(sock)


def print_result(result):
    total = result[0]
    print(f"Matched: {total}")
    rows = result[1:]
    for key, fields in zip(rows[0::2], rows[1::2]):
        data = dict(zip(fields[0::2], fields[1::2]))
        print(f"- {key}: {data.get('title')} | tipo={data.get('case_type')} | score={data.get('vector_score')}")


def connect(redis_url):
    parsed = urlparse(redis_url)
    host = parsed.hostname or "localhost"
    port = parsed.port or 6379
    raw_sock = socket.create_connection((host, port), timeout=10)
    sock = ssl.create_default_context().wrap_socket(raw_sock, server_hostname=host) if parsed.scheme == "rediss" else raw_sock
    password = parsed.password
    username = parsed.username
    if password:
        if username:
            command(sock, "AUTH", username, password)
        else:
            command(sock, "AUTH", password)
    return sock


def main():
    redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
    query_name = os.environ.get("VECTOR_QUERY", "fraude")
    vector = QUERIES.get(query_name)
    if vector is None:
        options = ", ".join(sorted(QUERIES))
        raise SystemExit(f"VECTOR_QUERY debe ser uno de: {options}")

    query_vector = struct.pack("<4f", *vector)
    parts = [
        "FT.SEARCH",
        "idx:case_vector_json",
        "*=>[KNN 2 @embedding $vec AS vector_score]",
        "PARAMS",
        "2",
        "vec",
        query_vector,
        "SORTBY",
        "vector_score",
        "ASC",
        "RETURN",
        "3",
        "title",
        "case_type",
        "vector_score",
        "DIALECT",
        "2",
    ]
    with connect(redis_url) as sock:
        print_result(command(sock, *parts))


if __name__ == "__main__":
    main()
