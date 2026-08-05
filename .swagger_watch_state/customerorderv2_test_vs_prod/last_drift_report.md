# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-05T01:13:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `569272e5e811c64e1cce022470723d360255bbb7cd486d7d4e874f2c5e8164ba`
- PROD hash: `1f782a8f5fc663212fc3bdef89fcd9adc6bac97868a949dd9f4d3780f38dd240`

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
