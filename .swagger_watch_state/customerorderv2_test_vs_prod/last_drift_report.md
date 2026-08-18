# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-18T18:17:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `70695f7edb4355ea649883284d85c66d5e677ff5311fd7b2574609914eaf9c29`
- PROD hash: `652961363cbc667283a6df541ccbdf3feab62e49cd2a4da9c83eaf4fcf1d75bb`

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
