# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-25T06:21:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e91dea365f9981a44071e9cf186258adc7052be618b82e27ac2b618753ce59b`
- PROD hash: `c1ed3f3fe48302738569b470ea0ba78391a4fc7b0400a90b52cb0a55b6fea4c2`

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
