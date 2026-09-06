# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-06T09:44:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `303f10b32c07cbd21a6483b32a9071d6267d7c14fb94cc77eeac1c4bd9657e50`
- PROD hash: `8180c73c5100ec06655d39d08da87624bb4064e6127df26e44d8341b2faac6e6`

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
