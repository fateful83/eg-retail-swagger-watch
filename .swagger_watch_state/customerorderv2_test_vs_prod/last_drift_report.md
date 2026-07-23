# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-23T18:54:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e3a58118f71220364c4a484b5710476ac3b58044dbccc68bd10ae23e48866c84`
- PROD hash: `eb3f88a74d921540458a182d779213be98933fd8b2a77c8fe59bf826d87249f0`

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
