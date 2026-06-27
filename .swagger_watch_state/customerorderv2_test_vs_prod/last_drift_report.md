# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-27T08:21:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4cdd7a6695bb1a499b7ebda87784a5be491378b2b9e3cdafcc9b4176bdd1cf2f`
- PROD hash: `551c0e1a2d5a2db2e889ca74c0fbaa6f1702fa8ca35e88df019ec32ac94ab75b`

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
