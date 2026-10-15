# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-15T15:49:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cb5f3a86c586db3c9b3fa5e74bf6c207b12e94fa84feecbe033f67a164a20f18`
- PROD hash: `db6477c85fb344ddfe9510e9441ff3b9a7b7bb75c2ac5f97cdf8cbfd0691bbb0`

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
