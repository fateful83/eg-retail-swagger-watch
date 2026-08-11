# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-11T12:33:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a50442c48162f4c57031a98b58ea7c740b298f86c3ba50df79e041409270da61`
- PROD hash: `f0a9352cf35375899a6cb845b4d557cd59f402351d058bb69bf7a241a5a2350b`

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
