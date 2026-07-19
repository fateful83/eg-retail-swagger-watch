# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-19T07:52:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c3f9f909a2c4f7a9f9f21c76e85b937c66c727883ee2d6c1f082518cf865f92f`
- PROD hash: `a7b06a18755bcda9090b874584cdbcf8b125fc91cf3913ef526d298303ec6f27`

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
