# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-19T00:25:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b452f92e76cc8ecff7ee850ed9fab0da94ad9b249240f01d25da9e6d43e1193`
- PROD hash: `9a90197582a3f10298a0965a38ec465bad690f2072e1ac5d542ec6889a1777ca`

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
