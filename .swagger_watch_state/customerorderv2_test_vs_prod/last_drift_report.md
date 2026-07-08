# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-08T08:01:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6105f46d160d8c4e0ceee03d0c39a8968cf4fcb0a804e04d4da16e10b3296645`
- PROD hash: `1f928e343c83eac1aed187e724664e18528f51693c806ec6e48e458c3e5f3abb`

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
