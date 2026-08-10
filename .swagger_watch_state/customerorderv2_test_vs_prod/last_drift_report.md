# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-10T18:37:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e8334ed6e1358c2c88e5ddc61d648308c9bca80fc78924d13680e41e62fb5415`
- PROD hash: `b82c806d3c5a91b00e8c2003484a4d6acded0cf12bee4f309c6370b271531b61`

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
