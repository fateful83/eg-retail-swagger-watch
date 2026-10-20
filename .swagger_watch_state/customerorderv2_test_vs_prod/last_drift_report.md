# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-20T10:28:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `930d6eaedd38ff015a6a8632208a4689b3d3e6f36bf53d87629d56e4dcc46a72`
- PROD hash: `0f812aaa1bcde4ba95f5b2f5d791c47c1e732b2b34b4430733e85bc2b0416947`

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
