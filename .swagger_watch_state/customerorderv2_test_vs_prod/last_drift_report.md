# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-28T02:04:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e1121ccf4aca235ed0736fef720125ee83a5d16a3def9c1688e7e0797699caf`
- PROD hash: `9c2ec158be2361af0323d05a294a123478479be9c5fb779dc7bb8bdb7d06bae7`

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
