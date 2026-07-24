# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-24T08:01:13Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7ca5ca71097678803a2c84fc409df8b38a2278a3cfd0a789838b57e009ad69b2`
- PROD hash: `804d6a748b1a44dcc6bb7865dbe3bb8a535515034a7601b93c9950a26f0006da`

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
