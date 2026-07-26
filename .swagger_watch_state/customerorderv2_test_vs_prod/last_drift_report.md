# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-26T01:20:13Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `969d53d99610db2b66421a52d9eb453001e23b8e6b84cedd116ce34383bca839`
- PROD hash: `e56148bec4a1999cc65d9761601b0083caf6915f64149364d3454fa196951f71`

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
