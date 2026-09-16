# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-16T01:48:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1685b630251698af12ed9d5a45201762239300ad2ca2f23703ffcf157cbcc104`
- PROD hash: `f65e741c8836f75b77071d1b88f315f304ed1f4c9e537e5603be87b4060cfe53`

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
