# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-17T15:43:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0775e2d9f528c08a09a9749250f4b23f45a4e911744e9a6fbea3aa797a21512`
- PROD hash: `c1cb2bb832037f8bda78fdfbae96e0ff1d52d91f9dcb9d9b1ed25b8e72377304`

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
