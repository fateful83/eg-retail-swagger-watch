# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-24T06:29:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3838332030213cdc3c6925cb8673e06c899fcf10e7043449cb866d7760826eb6`
- PROD hash: `d43400433dfb1d4203a09b050cfa15399e74bb3e116da649bad2616ffe4abac7`

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
