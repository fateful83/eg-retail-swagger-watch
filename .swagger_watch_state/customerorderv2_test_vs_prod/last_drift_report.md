# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-20T20:56:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9bf48a7ef4d1cfced0cb08107bf250a9e7e4341706f1b55f950c0e29a8508ec7`
- PROD hash: `c9c89aeedf6747ebef9fbaee60a84f7845805f6bcd63fe7ce86d660b7d232a9f`

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
