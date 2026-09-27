# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-27T20:29:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `737b0e62cb8b78793c9072a47d976835999e051a8f520715537be20462a58899`
- PROD hash: `350d9e1cbda520c55dcb3d6206fedd27ba60dfa5cdf3451f3c878cec24a388a3`

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
