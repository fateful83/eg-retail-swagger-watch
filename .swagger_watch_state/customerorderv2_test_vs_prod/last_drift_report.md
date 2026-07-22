# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-22T18:52:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7d816ca310bf7370483a1dc860c8fcd8b4852cae04ec93c791f0fdfc0c693908`
- PROD hash: `fb7695f272c2f4097c6e9a59b7551528a6d576e4354b2c4c45b01728bbd9afb6`

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
