# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-28T12:04:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `de1483b4661c2eabac5dd6aa6d215898515c8650ccae9275875ecedf8f38718f`
- PROD hash: `1fc6b1ec8f9d08be8e4ca8643150a5253801ebfb85a870a54c89847652435405`

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
