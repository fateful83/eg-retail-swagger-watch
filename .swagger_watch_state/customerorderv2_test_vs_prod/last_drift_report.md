# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-18T00:25:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ea3dde982f165afcfaf6d36fd138df29349930a6643a4449f1e5a38cec27a72f`
- PROD hash: `e700d4b96967e8eaed52be64a3fcba5ae94a5ee67f2f86c22bd01cf70fa7dae7`

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
