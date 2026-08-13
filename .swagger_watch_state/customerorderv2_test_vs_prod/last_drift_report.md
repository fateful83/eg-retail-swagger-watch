# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-13T12:37:18Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `93aff5c1013872ff826fb008685355b1d693f3afaa4af4c3f98e164478dae2b5`
- PROD hash: `9e28495e09a826ebee40a65fc80b6a19b31d5fc4e7f925d517dc9000eca50977`

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
