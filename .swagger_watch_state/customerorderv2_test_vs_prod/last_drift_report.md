# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-10T19:10:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `62e63ddac67cac1e430688b1869179468b2758ec0eecf80a0ddd73e5eb5fea69`
- PROD hash: `7e93b8568c469c0271c3979e67dac76634485a7809db8e3dc4e009f60b84ba03`

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
