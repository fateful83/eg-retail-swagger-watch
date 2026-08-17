# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-17T00:25:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7e494c7edbaf5a86ce1b61a0edeaf70b98b05e9f25fb54500c67f3369e5308bc`
- PROD hash: `e05a6437c90a98df7f92a21f4a945d519a8a0131af4037340a312a822c3397c7`

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
