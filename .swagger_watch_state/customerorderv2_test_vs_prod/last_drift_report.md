# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-07T01:22:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8d3574ccb9f00f98e71c13d5d643830416cf0e012a725f34c88f072bfc083a73`
- PROD hash: `72157e07b4f309c0427add8834ff9f6ab8eb0edb7ebf9b17d84d16e8b58425df`

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
