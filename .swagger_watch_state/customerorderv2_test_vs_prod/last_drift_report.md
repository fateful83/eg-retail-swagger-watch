# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-16T12:11:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `42111903406f37b037399bf8193c7d83ce6832474dcac1a6e6e1a117a8b3e6c2`
- PROD hash: `5f66dc5d2731c7e21737cd25643464010f2515d87e70b86ae26a78c0155475ea`

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
