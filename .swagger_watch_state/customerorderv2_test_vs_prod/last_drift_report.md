# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-30T21:34:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cabb2c5b1318f16d84326a96d0b36041f6702da1526e2627c4519209123515ac`
- PROD hash: `1ecf5a2ced4a9243092587b7f38f53546f51e991ae2f2f4c0fea920d96631d0a`

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
