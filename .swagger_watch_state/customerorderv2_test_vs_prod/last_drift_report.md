# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-03T15:16:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e27033c8ea03a7acd53776262fe810b5523551708006ddd5d4a609aeabfc4c72`
- PROD hash: `274d15fc7835d3aae9f0d8fe4c4b07980296fc2f2a6fe970a13cdc7a04863b13`

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
