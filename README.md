# Redis Search and Query Workshop

Material practico para un workshop de 40 minutos con clientes de banca.

## Datasets disponibles

- `data/*.redis`: version HASH para el workshop principal.
- `data/json/*.json`: los mismos datos en JSON legible.
- `data/json/all_json.redis`: comandos `JSON.SET` e indices `ON JSON` para cargar desde RedisInsight.
- `queries.redis`: queries para la version HASH.
- `queries_run.redis`: las mismas queries sin comentarios, listas para pegar en RedisInsight Workbench.
- `queries_json.redis`: las mismas queries contra los indices JSON.
- `queries_json_run.redis`: version JSON sin comentarios, lista para Workbench.

## Como usarlo

1. Crea una base gratis en Redis Cloud con Redis Query Engine habilitado.
2. Copia el endpoint en una variable:

```bash
export REDIS_URL="redis://default:<password>@<host>:<port>"
```

3. Carga los datos y los indices con `redis-cli`:

```bash
redis-cli -u "$REDIS_URL" < data/setup.redis
redis-cli -u "$REDIS_URL" < data/01_banking_documents.redis
redis-cli -u "$REDIS_URL" < data/02_banking_products.redis
redis-cli -u "$REDIS_URL" < data/03_branches_atms.redis
redis-cli -u "$REDIS_URL" < data/04_autocomplete.redis
```

4. Si el cliente solo tiene RedisInsight:

- Abre la base de Redis Cloud en RedisInsight.
- Entra a Workbench o abre el panel CLI.
- Pega el contenido completo de `data/all.redis` y ejecutalo.
- Alternativamente, usa la opcion de bulk upload/import y selecciona `data/all.redis` como archivo de comandos.

5. Si necesitas repetir el workshop en la misma base, limpia primero y vuelve a cargar:

```bash
redis-cli -u "$REDIS_URL" < data/reset.redis
redis-cli -u "$REDIS_URL" < data/setup.redis
redis-cli -u "$REDIS_URL" < data/01_banking_documents.redis
redis-cli -u "$REDIS_URL" < data/02_banking_products.redis
redis-cli -u "$REDIS_URL" < data/03_branches_atms.redis
redis-cli -u "$REDIS_URL" < data/04_autocomplete.redis
```

6. Si quieres hacer la version JSON con RedisJSON:

```bash
redis-cli -u "$REDIS_URL" < data/json/setup_json_indexes.redis
redis-cli -u "$REDIS_URL" < data/json/load_json.redis
```

Con RedisInsight, pega o importa `data/json/all_json.redis`.

7. Abre el sitio local:

```bash
open site/index.html
```

El archivo `workshop.md` contiene la guia del instructor con tiempos sugeridos.
