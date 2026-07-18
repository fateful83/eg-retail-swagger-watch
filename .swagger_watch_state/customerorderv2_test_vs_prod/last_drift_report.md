# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-18T12:41:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9108d65d1fbff4dd0f3a89f7bdd7f746e88912aeb8ed3d04322a44f2728c6fc9`
- PROD hash: `47c60ffca869489cfc30019109e8007df3a96258d1df4b8d2af9e0dd9cf6342d`

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
