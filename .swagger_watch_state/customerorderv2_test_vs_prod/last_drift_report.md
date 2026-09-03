# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-03T20:11:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4ca1914e7e525aa5f148a6d15614619c07ecdc5cb4d6c400ebbda3a6ece35ec`
- PROD hash: `d030f158b9e621a4d657e616a19bb69566858be972e48f6b66016784b3d759c0`

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
