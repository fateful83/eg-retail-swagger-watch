# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-08T01:31:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e18dc6f2f8d83bbbffc2cb0fbe3b76852878385320ac62514c23f4d3f928463c`
- PROD hash: `ac9c38c7fb6312329883005f2faab89ea4732430ee1e147d426c8e6be58e73e5`

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
