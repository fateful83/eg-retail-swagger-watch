# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-19T01:13:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9d2f31822d91f9d0411ee68fe3922fbb6b35b949c3727d19187aae633809dba0`
- PROD hash: `1f02d50f6db3ce462e9af255f955f1a818e9a7d2b137e9498d880ca33db0389f`

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
