# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-30T15:30:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1665b379949c4d8af8d4cdad55096bfbc1ba1575222d9e22fcf412441e0d0a05`
- PROD hash: `152888a695f6ac91bbc5d0f26185434971e76b8c861627865a6006c408487c9c`

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
