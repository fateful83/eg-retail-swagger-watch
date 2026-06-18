# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-18T20:02:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ba7cc56d1124bf0cada010358d71a7921ee4f65268cbd00f8c9c70448f32427d`
- PROD hash: `1351e1175a5260c515f15ed03eb5128f50c595690b108ca8f4924b6b134f0e12`

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
