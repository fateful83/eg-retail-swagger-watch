# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-19T18:43:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fe7eefef51936c1eae1ee90da58878fd1cfefdb2f2c5c0e88f517b452dcca954`
- PROD hash: `e40c32c87c234794cc5c3ff41c8afe9cc1f4542f68358fa0532f775519338672`

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
