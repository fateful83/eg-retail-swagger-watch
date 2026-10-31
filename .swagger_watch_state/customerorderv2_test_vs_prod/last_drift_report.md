# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-31T11:16:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a7d8b9b2f92d9bfa88a157769d6b5d44024248f869dd32c5fcf1abbaf8f81844`
- PROD hash: `dcdde14e602b63e25e1d97a6c0873667544e3d5341b45ae638d11b920a3135ac`

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
