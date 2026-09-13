# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-13T15:07:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0c9cd7bcee792f4b43bd09641641655bb1f9eaa8dceb29d0bbd29f284a697481`
- PROD hash: `4daccbe8d72eb7ddcdaf18fb754ddebef8328fc2396c792268bd324055ba942b`

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
