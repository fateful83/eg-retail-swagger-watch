# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-10T01:34:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c706ba0f6844a7cbab18f7080e702e779bfd29ec47d95cc9046b4a7c570baae5`
- PROD hash: `843bf0304587f1055de3358d7c7cd8ba9cd85d5f8c5f083eff2350437d3384ba`

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
