# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-06T14:27:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `05f1999514f95c1c38cfbd1e57c8374011f94545450efc842359e5e22d992294`
- PROD hash: `1519066a304f4d4ba3a9dcf1a74e19a25132e79c3afb4ae90b6daea59a34fe6d`

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
