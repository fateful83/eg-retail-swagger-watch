# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-10T01:20:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `98db5a4b15484d3104a3432dedf1db68ca09ff73a7246c3aa48acaa3fa082a87`
- PROD hash: `acb79a14aaf49d3811731571b243fd31bb15307e0e482cf8535fd5127cf90fff`

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
