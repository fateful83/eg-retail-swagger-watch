# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-21T13:07:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `90ae6894cef3aab133489dcf47a410260c42d2b27c7c1397c46e276c05e39358`
- PROD hash: `b25e2dc597d19389f0d92fc66cf24d5ca1c82fbf90f49cdfa0fceff715b81a69`

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
