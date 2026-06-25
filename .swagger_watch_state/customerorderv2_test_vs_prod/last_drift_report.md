# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-25T13:53:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0eb5e6883b54432ae7b6aab9f23aa9c2d219398471e74b58e17172dde45c878`
- PROD hash: `39084938c886dea8bd04771caa18e5c41e9d02d1270fcc8abbed5dd14c0047f4`

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
