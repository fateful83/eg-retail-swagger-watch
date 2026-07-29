# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-29T01:14:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ee19f49a2ea997b8e226c8be845d44893b16f87d2f2c66c30fe6cc7c13e81a77`
- PROD hash: `663f20ec58886f1fbee34e1a0146cf3f09a8b2d3f7ab0de671c8a9e21b4f40d5`

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
