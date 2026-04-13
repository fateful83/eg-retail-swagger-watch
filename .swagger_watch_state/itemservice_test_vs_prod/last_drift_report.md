# TEST vs PROD drift detected: ItemService

- Time: 2026-04-13T01:14:10Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f56a5e4ce2115ed72ce024f452ee443420ebc9fe3dc236db8561899a524053dc`
- PROD hash: `f9c7e9608fc43adbe29e64dee2db20c086e35e6d61a6d3c1b58642916401afda`

## Summary
- Only in TEST: 0
- Only in PROD: 1
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- DELETE /api/StorePrices/{id}

## Different in TEST and PROD
- None
