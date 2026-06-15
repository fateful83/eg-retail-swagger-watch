# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-15T20:41:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a86126a685f7ade2bf0e40066464b2addf9caba2eaf2eba20804eaec8416a6f1`
- PROD hash: `ec6ef987827aa3fc9a60484ca9ea2210fae0d053c6664aa97c1aa7fa7eb43f90`

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
