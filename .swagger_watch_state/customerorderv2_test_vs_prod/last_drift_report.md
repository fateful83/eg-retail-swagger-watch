# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-16T18:51:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e5c0b641218569ff1524ee4f7929a7c76736719c7d60291e4db7fbcea942b80`
- PROD hash: `447ce2a8d29f8319bceabc22419a9cd414470e2053f36e63e29a5994e9686481`

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
