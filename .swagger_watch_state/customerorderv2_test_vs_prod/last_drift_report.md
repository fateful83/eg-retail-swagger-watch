# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-24T13:57:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `34460077c6f3661a049359f63c71dadf7c7272a170765d4c5d7a7c38ce2bdf2d`
- PROD hash: `a3eab55910b2150347a621215e4ae1e148d853f7254359751d21a337b86bb448`

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
