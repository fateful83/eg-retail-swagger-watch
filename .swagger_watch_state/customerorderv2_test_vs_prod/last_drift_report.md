# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-30T19:04:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8a00932c37de14d9fce26815fd2d720e89e750d523c919baab8f63add788b420`
- PROD hash: `254982138e571975d287b51ea1339c46c387d155ad2bf44f26d5782bb5fbfeef`

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
