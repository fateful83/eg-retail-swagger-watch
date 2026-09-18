# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-18T15:14:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2c6641676953f46fc56824589799b26aae42054614274410fc8e704219cdc5c3`
- PROD hash: `dff2d01d711b23693188ea2191ba27c5ee29eb351e630e3a3dcbee3007f17619`

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
