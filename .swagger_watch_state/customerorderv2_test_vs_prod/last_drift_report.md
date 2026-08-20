# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-20T12:18:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8951e7bde44e25e8c6a6e011a630a947a89c4e570fd65cbd37c148bdf47ab4d1`
- PROD hash: `f00a356b219257ef7e5efe5392ed8e1dc1a9f63673304a648f45d9ffeebdf6c0`

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
