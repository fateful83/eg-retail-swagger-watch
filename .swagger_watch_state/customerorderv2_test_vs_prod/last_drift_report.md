# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-03T10:42:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `98007f7f5eb3b492dc92be71723d7aa69ccdc7fe5987e6b4f2926ef5ad6c1ee2`
- PROD hash: `aa5bf5f70d7724dfb7085bd116e3d2c376c4e0083138eab72cc24a8edd4778be`

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
