# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-25T01:54:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `92c8d9c7ab9eb40e0d5172fe22a5b77e5eb7f96d26b0ded8f7b611307e423849`
- PROD hash: `b3fe72980e13a04e32219001d94907a05cc8e777318732d88946c50ab1465dc4`

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
