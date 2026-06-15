# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-15T11:37:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `776c1beff359b60b1a8aeeb427e4cff5e1cb10618e26db7c2b1aba915b590253`
- PROD hash: `a34553fd36695588bab3ee7a762eb1a1d6d8415edf1d2d27908f2142d2f9568c`

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
