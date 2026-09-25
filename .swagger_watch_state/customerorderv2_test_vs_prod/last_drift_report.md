# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-25T20:47:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `22e9790dcb8dc7c6107d7ed6753b2188b0aee3f4a6e3f67561773c0073976ebc`
- PROD hash: `03ba45239a290a38976faeaab4fbd21f0792839adfed106b4b239a611cae789b`

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
