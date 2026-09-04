# Redis Search Workshop

Material practico para un workshop de 40 minutos con clientes de banca.

## Datasets disponibles

- `data/json/*.json`: datos del lab en JSON legible.
- `data/json/all_json.redis`: indices `ON JSON`, comandos `JSON.SET` y autocomplete para cargar desde RedisInsight.
- `data/json/vector_cases.json`: casos con embeddings pequenos para similitud vectorial.
- `queries_json.redis`: queries comentadas contra los indices JSON.
- `queries_json_run.redis`: queries sin comentarios, listas para pegar en RedisInsight Workbench.

## Como usarlo

1. Crea una cuenta gratis en Redis Cloud: https://redis.io/try-free/
2. Crea una base con Redis Query Engine y RedisJSON habilitados.
3. Abre la base en RedisInsight.
4. Carga los datos:

- Abre la base de Redis Cloud en RedisInsight.
- Entra a Workbench o abre el panel CLI.
- Pega el contenido completo de `data/json/all_json.redis` y ejecutalo.
- Alternativamente, usa la opcion de bulk upload/import y selecciona `data/json/all_json.redis` como archivo de comandos.

5. Ejecuta las queries:

- Pega `queries_json_run.redis` en RedisInsight Workbench.
- Si quieres explicar cada bloque, usa la seccion 3 del sitio.

6. Abre el sitio local:

```bash
open site/index.html
```

El archivo `workshop.md` contiene la guia del instructor con tiempos sugeridos.
