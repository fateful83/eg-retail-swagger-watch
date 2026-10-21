# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-21T16:10:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `31648e30ea0e7583e041e38bc60dfafbf1774881d29c140c2c9c7be844391b06`
- PROD hash: `bf7b1bbbeb6d31e1c54a1199e27ee13400ecdfab1a1c8e923b42b06cd2253236`

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
