# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-24T20:50:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `39cc591b3065d51458fd2c90139b6e214004f566ebcb0dc34bc09bf626f1b874`
- PROD hash: `24c567658e87b3fc3dbc22b9fc52bf77d176c61985d939fb05dc322eb2e84166`

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
