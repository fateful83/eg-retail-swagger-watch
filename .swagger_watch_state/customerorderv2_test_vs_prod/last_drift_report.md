# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-18T02:07:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `13b23852a52ae209107bb1b6488b5b52c30d1987bb1d89fab2971796fdf40f2d`
- PROD hash: `20086409e21b74f37845b0ad374e646fb695bc4e2eda47ce22fbde7a59451c5c`

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
