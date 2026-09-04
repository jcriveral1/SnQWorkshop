# Workshop: Redis Search and Query para banca

Duracion: 40 minutos

## Objetivo

Mostrar como Redis Search and Query ayuda a resolver busquedas, filtros y agregaciones de baja latencia sobre datos operacionales de banca, sin reemplazar necesariamente a la base relacional core.

## Agenda sugerida

| Minutos | Tema |
| --- | --- |
| 0-5 | Contexto: Redis como capa de busqueda rapida, no como core ledger |
| 5-10 | Ingesta de datos HASH e indices con prefijos |
| 10-25 | Busquedas de texto: ranking, prefijo, exact match, stemming, spellcheck, autocomplete |
| 25-34 | Filtros operacionales: multiples campos, rangos numericos, geo-radius |
| 34-38 | Aggregations y faceting |
| 38-40 | Cuando usar Redis vs base relacional |

## Datasets

- `kb:*`: documentos de ayuda y politicas bancarias.
- `product:*`: productos financieros para busqueda facetada y filtros.
- `place:*`: sucursales y cajeros con coordenadas.
- `ac:bank_terms`: sugerencias para autocomplete.

## Mensaje principal

Redis Search and Query es ideal cuando el usuario o una aplicacion necesita encontrar, filtrar, rankear o agregar resultados con muy baja latencia sobre datos que cambian con frecuencia. La base relacional sigue siendo la fuente de verdad para transacciones contables, integridad referencial fuerte y reportes regulados.

## Cierre recomendado

Usar Redis cuando:

- La experiencia necesita busqueda interactiva, autocompletado o filtros rapidos.
- Hay consultas repetidas con latencia estricta.
- Se requiere combinar texto, TAGs, numeros y GEO en una sola busqueda.
- Los datos pueden materializarse desde sistemas core, CRM, canales digitales o data products.

Usar una base relacional cuando:

- Se necesita consistencia transaccional fuerte como fuente de verdad.
- El modelo depende de joins complejos y normalizacion.
- La prioridad es auditoria historica, conciliacion o reporting regulatorio.
- La consulta no esta en el camino critico de experiencia o decision online.
