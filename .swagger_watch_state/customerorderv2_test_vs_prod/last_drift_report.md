# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-04T08:15:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `483953396df21e593ddec4d9c46f669a623d66d8f958d6477d26ba6fb72c897b`
- PROD hash: `6a87094b2c6efec403d03e9b8cca10a5bfc6b72228f4c0030271fc9aae6afc9d`

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
