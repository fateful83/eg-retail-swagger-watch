# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-22T18:10:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `37555e8c0fd3b83dc92a5442d6f33138b0e9873fd1e31e05b2fc9cba67b81046`
- PROD hash: `acccc720bb2c1f89279d9cbd9c1b3ae58dfa30ca289fa63ced8306d5bd6ea47d`

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
