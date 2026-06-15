# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-15T16:47:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bf3de305ad2226b90cac274e4929b686a1d39ab1a5f5db249201ff9b0dd2d995`
- PROD hash: `979973c7457b96b3214cc2113b20051b47f5577f5d976e86467083cce1e07390`

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
