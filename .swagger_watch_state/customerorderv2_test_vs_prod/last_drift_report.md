# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-29T11:49:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bf5951692b956a1ec52e9385b08188a90a31448ba533cebc3a641a511b9842f0`
- PROD hash: `4af4b4373682f0cf97441115f5f5232bd271751d5446527060ccb15c0e90ddbf`

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
