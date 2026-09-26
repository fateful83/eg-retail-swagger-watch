# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-26T15:10:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `549861a5e2d8ad5b92c865e098cdd59375555997d3f268fdb204ab9c764cd1e3`
- PROD hash: `a962e5937b12a4d6d9cd61b006f0a4bb3e5c4fbf85d2e3865aef0171d385cfa5`

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
