# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-29T19:28:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6cf3e86968ac41a354cd334ca8f2d03bd4ab756eb8eedf051c1e811152549b71`
- PROD hash: `e8d723b62d61d2ce37a7a0de0aab4ff033951962a6e46ccc090992010afe2956`

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
