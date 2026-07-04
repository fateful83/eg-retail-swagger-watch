# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-04T18:47:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5a020ff18a1ff03033b61240ea5d6477ae02d019be31dffc3425e5259f27b2d0`
- PROD hash: `5aaeb37db92a3eed7900c81ec1d0f78d7d8b034cbf3a951822e9c97200a7c9f5`

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
