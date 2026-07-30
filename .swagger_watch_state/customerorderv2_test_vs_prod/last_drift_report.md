# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-30T08:01:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `81cd49234ce7b5215b75bb82a945a8065344ffa5e361d3ea33de445aa702f0bc`
- PROD hash: `6eaba9c54fbbab4f64b428ef7e79c26cd9b038954fc587f95c9a74b28758a2d4`

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
