# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-15T13:01:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `812ca85c630101f4ae1c94adf6064b9b465bc2f771c1933cb8b8996b41890b67`
- PROD hash: `59447d008d3c882d3ccc250f1459662381cc11005de26f760c4b0219b77f8646`

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
