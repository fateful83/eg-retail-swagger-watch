# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-13T01:30:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `211f0062ef89d7ec93170dfccd1870db506e3615c7a9ad77bfccd13126ffcf05`
- PROD hash: `f7200e35d460f0acfe8ea450e16a8907ed83dde8e2dbcc5e49b11440a714ec95`

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
