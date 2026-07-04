# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-04T12:51:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `646fbe34b74b08565b9186abe5ee35f3ff18d25120191ee4c6fea63c8b1946cc`
- PROD hash: `3b996b4da9640de8362bc145e64493e0e8640d58ac612575eb3454ef6a9cac27`

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
