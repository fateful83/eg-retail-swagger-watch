# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-29T01:12:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `613ac75ab1ee759c3e3bb0434a8b778770b2ec6177f46263f89ec9858cd7cf3f`
- PROD hash: `cdb9ffb6cf1312512e190f2bc77ce214d1a7262c53f8a557b45d255b60347397`

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
