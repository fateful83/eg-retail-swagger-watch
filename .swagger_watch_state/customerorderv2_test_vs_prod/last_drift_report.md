# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-25T18:44:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2fb6936f2ad369cbf1af5898064b258cd53106c6cd9d25cdb92082c5f8a4ecc1`
- PROD hash: `e02be14ef1633ac88288dbe4908619a3a6923bb6f55973ff5acb0050e7adeac0`

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
