# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-03T10:10:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2db298e25d8df5fd5040aa04a83320f7d017488ffda88989ca3efa5c96f4b404`
- PROD hash: `56d9f975e9617706c3540cc52dfb7ffde8d75ab071cb11f5c3df324fa8360770`

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
