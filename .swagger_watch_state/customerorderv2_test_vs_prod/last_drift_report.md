# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-08T00:37:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a50ca43ebdb7d7a2f9d69d82d02378ebe676c55d7539ae582287d4a044bf1de3`
- PROD hash: `a7bbc3f51c0e7de7f9fb67a4364d9d3e88c88a56aea694cddfc2f31a3080a311`

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
