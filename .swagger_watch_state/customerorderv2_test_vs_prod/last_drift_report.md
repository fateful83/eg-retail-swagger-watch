# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-24T10:34:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5bce0c4a730e7e330a8cae7831b3eafe25794340676f8472267efb423a6a67c8`
- PROD hash: `3946c09aa6cb66e79b0bf17f739c31d63af2dc90b747b3d7b5ae874b7b038662`

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
