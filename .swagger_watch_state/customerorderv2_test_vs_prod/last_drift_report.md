# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-17T20:36:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3fee8e1d2d1b73324d0ac881420b5e20db7de8a6ab85d04498458fe989db0c23`
- PROD hash: `9dc8438620afde5e22c1634987df1ca6ada3e02dbbf9d17f2d51eb818699de88`

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
