# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-01T22:02:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5bde32ea2dd2c818feba8a4938fb9edecb872b196a9c020ba3abd262793069b9`
- PROD hash: `a57bac766e300b92c8a8901c57322a8b0013a056067e86c5f2cfecf75a522f72`

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
