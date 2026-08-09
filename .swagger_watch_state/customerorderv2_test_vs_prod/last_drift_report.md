# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-09T18:19:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7a262802f9067d01803dcac120bc26495f336fe41f54f445f09983f56c3cd8b`
- PROD hash: `f6038ed06128ae22ba24724daaf17d87d2f2910436c9f49b661805959c83a164`

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
