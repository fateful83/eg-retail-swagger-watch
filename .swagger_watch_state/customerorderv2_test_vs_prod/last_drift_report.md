# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-23T02:04:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `66a6f5683231b0d3535061d4f93dc45ac968e503d5802255632a0525121c971d`
- PROD hash: `5aaa29b82974e9b592c598e42f391eff59b80c4c6edb7c0ede894750da5ffde7`

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
