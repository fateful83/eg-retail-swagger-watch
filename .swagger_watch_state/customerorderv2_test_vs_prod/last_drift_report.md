# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-14T11:01:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f772b423cf4083ad2de53b1eebfcdfcbe287389c950322e2ea6aa11051e65ade`
- PROD hash: `4a08d330ad1ea9db2ddec018ce5eecade9eb0b89abed5b83458e8fec7751aaed`

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
