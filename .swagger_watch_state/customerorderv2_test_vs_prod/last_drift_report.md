# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-27T16:53:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8287863d713c3321f4e32bd35e28c0b5906d9b9289c292ba6303df2ba5cbfddf`
- PROD hash: `60ebd0ba56f02fcde2efcdc30ceb26c97debbebc9904a837ac7c0a9e530fe8cc`

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
