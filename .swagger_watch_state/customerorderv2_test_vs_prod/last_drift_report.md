# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-23T13:15:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7f020b9adf32ddcf39dbd544a2b47539e262ba4fb737230509f9f6449f957d95`
- PROD hash: `5af4350d3897d134d0b1704efc5ae911a6fee75c65f4908a10dd2f87964802a6`

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
