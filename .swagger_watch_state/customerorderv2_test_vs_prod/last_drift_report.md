# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-18T14:36:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a8de8728a17d852c81b5e618c2a67c2cd6905fb8fad0a21f922f55f159aa4dcf`
- PROD hash: `c03f73c35f5881a1a5b9e5420acdce8d1ec3450e62cf19223edb20da10b3522c`

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
