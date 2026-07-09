# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-09T19:15:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `385d439edebbfdbceefe5e21574d2a1550b4d058aeb8d0f06843eb8e100eae86`
- PROD hash: `fcf49bd161e83eda6f63d94dacce027a510c5653f22d9465c21cac238220ab74`

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
