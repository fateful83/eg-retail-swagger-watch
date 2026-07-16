# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-16T01:13:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `90f8bbf4f4b2540787bdf031a3ecf1d94dd36883d027ec42f79ec842a1fce0f0`
- PROD hash: `c11e25e88096f586fb2f5a0da6373f48470c04594cb9219d7e1b22a08cd845d1`

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
