# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-09T00:39:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `df4ae30dcb8329c30c7ddf713a70056425b8edc3f7b09528bdc7510735c54b11`
- PROD hash: `5f79eb8ab4094c04e9a10ca14eed473d2342705260e391f07506a96d83d02409`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
