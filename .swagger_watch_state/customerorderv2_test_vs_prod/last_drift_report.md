# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-25T20:03:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `acb727df27622b6d98d70d7b2b5a2e3d50f1d7a4ac102a90bb070245eb2658a6`
- PROD hash: `9c879e9677b50960c02c72ea22620ace8100643a61a715e4ec41108fbdbf91a4`

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
