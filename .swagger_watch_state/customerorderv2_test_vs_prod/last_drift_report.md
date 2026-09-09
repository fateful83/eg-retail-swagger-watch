# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-09T10:10:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `01c55a4165e4223f3db9e82bf3f8205a6edcce41984babb6f00c8d8de5b96cdf`
- PROD hash: `f10d0ded7eca327c727b83c3aee093b4bdad4a48d2e2a5257e86944e29ff1748`

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
