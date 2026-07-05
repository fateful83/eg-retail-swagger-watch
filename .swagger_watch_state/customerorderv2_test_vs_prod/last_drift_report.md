# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-05T12:59:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e8ca3b2385b83ee6148d518b4a8e704e24c6d790167a88807602e06f151e63b`
- PROD hash: `5f33ab478c8fe5250df180da55d23035a34104f9ee78e5c3009888c9a7c322ae`

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
