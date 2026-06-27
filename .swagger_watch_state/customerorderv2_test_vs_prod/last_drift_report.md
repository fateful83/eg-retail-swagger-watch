# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-27T01:49:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c3b52e1f96f0ac6cd8d9ca840fbe81bffde4720e5ec68fd30f970aaaba789bac`
- PROD hash: `2ac4d561d2945b4293dbaccc4c3b5b43a4b823503778abc8c37d0cc77694177c`

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
