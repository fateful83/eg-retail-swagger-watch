# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-23T10:35:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `385194a67d55cf116d98f8ded1e86202ae1b8262d5a1c7fd5d4ca02d98d507d1`
- PROD hash: `ce2d25dea9c6442f83c765ecd03b39d41f53aee2a150a0fc1e6e81f7c032c7a2`

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
