# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-15T10:24:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3a9c56c5e60270fee1aa372636f6135b6095fac0e00e9cbd4e476fffbb4b8c51`
- PROD hash: `ee25407fd122a9d6dc50b5c9a0ce0074d7a60cc8ac5100b7f77f19b1b94ecf06`

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
