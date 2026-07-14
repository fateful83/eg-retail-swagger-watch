# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-14T18:55:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3f19346a3afbff2ddd55ad429370255d1b7c6ea86a3c59932754dde5cec9c34e`
- PROD hash: `e4569640998fc8f44a18d4c8f873b110e2da6f1c1348719103c8db2c5679e439`

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
