# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-05T01:30:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d53013892d8c296f80dd6290924cf3964d4aa940cb44fac952ac20d390c1265b`
- PROD hash: `d530b5f9d188de51616ae5a91ee35ecb550af467b92c5719d1af6d0c261fe3a9`

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
