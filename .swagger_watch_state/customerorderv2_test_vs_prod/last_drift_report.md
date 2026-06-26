# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-26T19:24:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f78e240cf67f4716282cbe66c85ea3ddaa692897f3b539e394052b6d38f656e4`
- PROD hash: `976c2b6aebffff584af9242efc5c57e45654dc37ae07d39625e52a98d94bca44`

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
