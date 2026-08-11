# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-11T00:40:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f9f4a7b604ea9078126b6cdd86301e4a1e4161c050dc4dbdf82c9576587783b4`
- PROD hash: `addfc8ce58ea28c2acadb425ea2b642abb7e56748ed4e4ad1c9b62f4ff713ec7`

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
