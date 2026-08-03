# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-03T14:07:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1b085fd05970c1e10de19a8407dac51ac3902a96e1465b2f92f7a8ed86bfb9fb`
- PROD hash: `c15293dc579df442affc73c872db4e88c56c1373c3a7165a1aea0f85863064d7`

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
