# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-07T01:30:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `994479426ea90a175eb37550ca08ed76c75c0bc66996d98f6491364a96cd3a1c`
- PROD hash: `9b5090b1187dff232aa7af6a959409c1b477013f4a7159a195085e049614ccf3`

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
