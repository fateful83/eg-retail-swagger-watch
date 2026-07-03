# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-03T13:25:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a5184428616604c3228185893c389312b9f2e252244978d7c98929f14c674f61`
- PROD hash: `acdceb7732e5b22cec64cca387c9b07e47fe75c4b7e29d76604395f42c69ce48`

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
