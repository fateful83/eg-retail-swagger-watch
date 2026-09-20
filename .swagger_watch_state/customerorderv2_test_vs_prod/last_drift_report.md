# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-20T01:46:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `99387b6997aedaea935ab8943a79bf6ef7d60c15c3862e24749f89fccc1b249b`
- PROD hash: `7f39cfa82f7da51540d73d2c878a86d8f9e0093547093a61cd6f0796a5e19836`

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
