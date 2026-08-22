# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-22T12:12:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fb77db69b454f90f3f835d708a07ebd0df43cf27a6ce09ea16e11056290ee83b`
- PROD hash: `f7641dfa4f27d96f3579b50d2494e419675d60eac19cac50bad98deebd588a23`

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
