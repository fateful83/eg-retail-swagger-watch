# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-24T18:19:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b09c14e86e6eaa0ff4f0bee8fb284c9dad55b2a8c8e9bb5d89d505ab09970939`
- PROD hash: `ebc93082bc417efedeb3f6a9c6a64b8d6173f14eabeaa434f0d6b954c905ab21`

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
