# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-30T01:55:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f6208931f9a7f79339f18bed4a0e2b0d050054eae6397b4dbd232ee6fdb12e82`
- PROD hash: `742cc23902ede0fc7364d97eb571857bc3de038b21d5e08570b9709ca023ecff`

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
