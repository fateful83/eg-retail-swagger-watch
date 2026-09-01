# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-01T20:12:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e20d1a8ab715b0ae32b861881195380978348cb3df06e1e7c2810409d96c795c`
- PROD hash: `dd7f033e7e48414358f9e93bca11e05db421849334c4313d9513528fd1371932`

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
