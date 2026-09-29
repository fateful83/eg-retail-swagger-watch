# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-29T17:04:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `28325751dabde7b309c518b6db964b548f00ec7fef21bb4c68cc259227fff3ec`
- PROD hash: `93c224e37f5431ed9a4b4bc72b455f8cff92dd7af740ffcbc130eb2fe23d98b7`

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
