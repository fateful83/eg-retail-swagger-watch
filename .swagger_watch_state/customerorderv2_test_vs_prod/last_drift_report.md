# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-20T19:03:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `39684de429a6e67a7e9796e069f8fef04fd215cb2fa4a964ed7a569d4a24d6ab`
- PROD hash: `f0079a2e944779a9cc1387a76319598ccfef0c3cd2a8e891f4bceeebfdb7b44f`

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
