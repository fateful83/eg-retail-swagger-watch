# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-05T19:36:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c387294fe5385e46a3640ee185aeaa83ea815f8ea52ce9c0d2e9ab7881e32453`
- PROD hash: `9c3cd9ab601dd52ffd1f6c5144ee431aeb5bc87346c65b64a21b93a90f6dc927`

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
