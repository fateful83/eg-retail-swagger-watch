# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-19T19:37:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `39337b78d2c9957a21d39d3ee49328b00c8934c2826a53e5f556129ab68ab7fc`
- PROD hash: `1948adfcca45db7f6042efd625f095cb2ebb55bd5f3f8124a73f78caaf3c308c`

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
