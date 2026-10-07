# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-07T12:07:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e20c247559ed53985ca5aa37f7d08b73593e1021cb704963b398b7e6e1fa6d7`
- PROD hash: `19547d8ef19252cf8d11378db04e19e02db2d749205636300d8e75e557ba1751`

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
