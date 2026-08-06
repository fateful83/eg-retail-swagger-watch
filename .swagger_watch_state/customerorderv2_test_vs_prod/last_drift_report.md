# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-06T01:10:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2fc3afb867e7e164fd6e0f58e3e781f3b0f6cebfc0214fc8d19e2fd06bdfb9ce`
- PROD hash: `c3c1f6e55c690c0aa501076b7b2f07ce0dd634e8989c367966b50718c2ac4566`

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
