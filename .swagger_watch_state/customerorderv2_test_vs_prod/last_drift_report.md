# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-06T22:35:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d447d7825d1284a42c5c93b8d4a1fac206493b09455beb134315a562036472fa`
- PROD hash: `feb155d6c2f5d1291570cd3a4f411a0da007ebbc45f4303a3899953fa42fc460`

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
