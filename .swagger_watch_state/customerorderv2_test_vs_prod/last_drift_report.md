# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-10T02:51:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f81c112aaa24b8a8f3bbc461a6cb24eceae8a7e4f0e695f886fe001911d53666`
- PROD hash: `f8ebd0a2442663ba79cd63f34deab4f6d6eea7232d3b257862d6899026e8f165`

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
