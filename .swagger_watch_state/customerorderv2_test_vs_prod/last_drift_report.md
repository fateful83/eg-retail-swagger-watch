# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-09T06:33:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `26e8896fe42d4fb9c88c3b9ac6876b218321411a9b171a238f10df3a904815ca`
- PROD hash: `d4d1b4609bd838cc535e3f997bf03b98a900eb6e78fdf4fa2a8d497845f40901`

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
