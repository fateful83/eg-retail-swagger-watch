# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-23T01:54:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c914c9d58796f66efc438a5c2c2a68c7f9621654dbb9a95974ff543da5db8721`
- PROD hash: `31ea597f4a6676c545da07c4ac329b77ce661977eae862dcccbbfc378eb820d2`

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
