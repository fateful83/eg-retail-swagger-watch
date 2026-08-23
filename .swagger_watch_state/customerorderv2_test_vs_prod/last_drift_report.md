# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-23T06:18:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `57452f568a3f5b980a1e7bb663aed8c6edcef3a3f5167e30649baa30df1faec5`
- PROD hash: `d2ea16417b2735075edd62a37da4fa4ef23f6db41882770ff23e59deedad0edf`

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
