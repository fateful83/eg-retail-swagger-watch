# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-26T13:52:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `94a5eb2a4a3cc8cb05e661c88a183a5e18e38327289941df637b0d5ef7c86161`
- PROD hash: `5cade4bbc48a08ab22febf7c40a826d20772c2d4bf5470f35472268b07affb99`

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
