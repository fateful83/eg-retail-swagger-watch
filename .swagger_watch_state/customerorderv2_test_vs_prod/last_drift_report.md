# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-10T00:40:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7c3a28597acf4049a4be5de3036ad8ac047434af4f771fdf9fd995951af6e333`
- PROD hash: `530e23060e608d962ff9dfb37afda4dcf31476b3e0d44b33266faaea6bc097f7`

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
