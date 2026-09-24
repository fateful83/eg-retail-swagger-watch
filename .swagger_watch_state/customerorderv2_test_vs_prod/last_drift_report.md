# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-24T15:57:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e2447abfe740d0df82486e91fd0e8c565f6674025756fe46822de003621e6c89`
- PROD hash: `3e6faf1e6c3c4811b9c7cc4ef9723518389c5a4bb06390585c9d3a30beb1de6b`

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
