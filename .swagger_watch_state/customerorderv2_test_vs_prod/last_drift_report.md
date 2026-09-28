# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-28T22:40:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `075c538574bea4f7bb72f29ba261531cc487dc09eabb2f9750d3bc2f2fb711ce`
- PROD hash: `11cc1fb88b9d347f9a808a0c83cb08499bc659ec25b54e4beff08503036e0bf8`

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
