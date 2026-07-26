# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-26T08:00:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `34124cacfbeb497441186c8f8646bbee534eef5c51c5e52bde27c0091efe2f3f`
- PROD hash: `1f48d5c97affa31707b1a4a324fab053e1518ea1a2ff48664197b594bf21effa`

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
