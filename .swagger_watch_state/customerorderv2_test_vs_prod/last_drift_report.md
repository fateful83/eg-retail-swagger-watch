# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-26T18:48:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `089c69ce416eed01811c63c994d28ac17afe77065dcb2a730e9263ebf6878fd6`
- PROD hash: `79be80e6b05c6de96846d1448e691598532c33c543c4b8dd4c131536dc3a2365`

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
