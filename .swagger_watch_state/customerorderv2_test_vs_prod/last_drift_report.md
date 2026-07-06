# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-06T19:25:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `36fab5a057139f2664a275fba7fbab5d033f0defd2dd49557916f7b6e9231725`
- PROD hash: `ff2b2c044b669f5c5ff2f89721e1414a6abbd6162515a8c20d2164b0c7785abe`

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
