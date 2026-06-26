# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-26T01:56:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `31c6c1efe6a9c2113f2d5eb3fc6ace483a49695d2f6a92a46cf22c6b07fbc449`
- PROD hash: `fd30df6cae5545cc2bb8ab0d94055cdce9221de3d35f6eaf11f822cd86ab9278`

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
