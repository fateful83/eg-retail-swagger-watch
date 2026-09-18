# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-18T10:06:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b47df71df0f2992fffc5466450b15bd561f5ae2c465658bd3a68964d049905ad`
- PROD hash: `3f09a7417bb6351352ead3bb77dc4518c459b7bbb4a77e2bcaa8e10e31520a8b`

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
