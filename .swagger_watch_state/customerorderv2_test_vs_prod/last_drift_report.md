# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-04T16:01:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3509a6d208d458065fc9c9faf7198ce3086ce3aecd20b33d4d1c26ecee3042e2`
- PROD hash: `f733fa7f1e9f357124a3e44a4f78ef1f5c888defb5413a37cacb5cd30c197d59`

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
