# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-20T02:12:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e34406cac92982abe5b31a75259a3894f65950c6d5e9d0fe9e2ca5ccb10e28c7`
- PROD hash: `03cc9d373d1ace122d91391bcf5eeaa55529c839b2113f51dc6367054b8f9b17`

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
