# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-31T11:54:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `935c9860a47d9a6a6f507d6825ad80eb87d420263b0499cd39f88ac46c94a6aa`
- PROD hash: `8dcbc7b31a424bc88729af288a691b346d5e403eb6fcf4be140be68e49d4e5e0`

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
