# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-20T08:30:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9769165b8917776c914dedfe485a909a61fc6a180aa16cb6696cd78245b7d9de`
- PROD hash: `d15bd5712aae7378130a06fb6e3a84754a6bb2cae852eac322416712ad8ec329`

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
