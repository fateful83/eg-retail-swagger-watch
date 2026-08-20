# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-20T00:26:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `60b3f9b5c1b8e1e17f9697f12598fd081474dea0832718c556d92c5a8f0d5a26`
- PROD hash: `da2069a5232afd838f2fabb9152a1f58b49c4112425c4635c8a0e12748281d6e`

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
