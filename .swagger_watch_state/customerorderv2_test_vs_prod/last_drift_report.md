# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-25T10:13:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `42c5531c86cc36d6f7298b10e44c9d9251a82f79c5e4b36c96b6f13b1dcc9bd4`
- PROD hash: `82eb5506fad100cfefe3c7a9a0d18d48391ae8730eed37b1492dbfa32c1c5f87`

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
