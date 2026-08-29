# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-29T15:47:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `570bddb7dfcb370695bf03d59d99882556f01458220a8553974ab88ee6a6df3c`
- PROD hash: `492c6c423909c8de9f0fab8d2e12ffaf3e2c189cbcb09ac6deb58da81b0c74c5`

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
