# Workshop: Redis Search para banca

Duracion: 40 minutos

## Objetivo

Mostrar como Redis Search ayuda a resolver busquedas, filtros, agregaciones y similitud vectorial de baja latencia sobre datos operacionales de banca.

## Agenda sugerida

| Minutos | Tema |
| --- | --- |
| 0-5 | Contexto: Redis como capa de busqueda rapida, no como core ledger |
| 5-10 | Ingesta de datos JSON e indices con prefijos |
| 10-24 | Busquedas de texto: ranking, prefijo, exact match, stemming, spellcheck, autocomplete |
| 24-32 | Filtros operacionales: multiples campos, rangos numericos, geo-radius |
| 32-36 | Aggregations y faceting |
| 36-38 | Similitud vectorial sobre casos bancarios |
| 38-40 | Cuando usar Redis Search |

## Datasets

- `kbj:*`: documentos de ayuda y politicas bancarias en RedisJSON.
- `productj:*`: productos financieros para busqueda facetada y filtros.
- `placej:*`: sucursales y cajeros con coordenadas.
- `casevec:*`: casos bancarios con embeddings pequenos para similitud vectorial.
- `ac:bank_terms`: sugerencias para autocomplete.

## Mensaje principal

Redis Search es ideal cuando el usuario o una aplicacion necesita encontrar, filtrar, rankear, agregar o comparar resultados por similitud con muy baja latencia sobre datos que cambian con frecuencia.

## Cierre recomendado

Usar Redis Search cuando:

- La experiencia necesita busqueda interactiva, autocompletado o filtros rapidos.
- Hay consultas repetidas con latencia estricta.
- Se requiere combinar texto, TAGs, numeros y GEO en una sola busqueda.
- Se requiere encontrar documentos o casos semanticamente similares con vectores.
- Los datos pueden materializarse desde sistemas core, CRM, canales digitales o data products.
