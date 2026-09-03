# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-03T01:34:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d8fe227346f75fc4e4d3abb26ad40cbcdb8c168c032cdf24ba132d664170fdf5`
- PROD hash: `476a23bd564c7d778d731f6e591214615a7f3126e403b304154180e0fcb22715`

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
