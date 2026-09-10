# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-10T15:15:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dae85c94140c2d6cad6dea6f8b90da208359f70d1c2f5b98a228cedd6fe6522b`
- PROD hash: `748c1c9f0dd3689efd4781f1b9c2a7083d9953d97edb006bc3e125009a1391d6`

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
