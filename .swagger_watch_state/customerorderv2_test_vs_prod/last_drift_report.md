# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-24T19:53:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5a8b0a2d2e64f94862c4a56c9c29edb2e0a45d1d80fd4e6f8d3e1b0736cda508`
- PROD hash: `1c53e02915c5b55e4718f28850868a81b055fafb91c9047dfa694e853d56f62f`

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
