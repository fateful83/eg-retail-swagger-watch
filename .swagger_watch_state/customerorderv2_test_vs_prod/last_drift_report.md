# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-03T01:24:18Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `080298021a0d530f966340277ca88f9f4cc1e74a89c7ef1973e230d594e3c14d`
- PROD hash: `5d193339a4639dfd1d6da40b897298688511231de6cc4f9a9232491e678990b5`

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
