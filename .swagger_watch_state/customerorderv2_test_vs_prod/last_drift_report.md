# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-14T13:21:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bfd6fe1c001403957b790fe616b076d9ae32971d7f787db8ddb4738cee270a6a`
- PROD hash: `6ed2372789fdaa1f795372e2a26c9a2762e251cb2f898cae10425ff42b4779f5`

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
