# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-11T15:17:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3bddca5e7f131357419ccfa4062fcc8218884f9487416b2fcf0b3866f4e28e74`
- PROD hash: `1969653d4f93b9a059db8e34317b755ef8844bbc433459f902c1f325395609cc`

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
