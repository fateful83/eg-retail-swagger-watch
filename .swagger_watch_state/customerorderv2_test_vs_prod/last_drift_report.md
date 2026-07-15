# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-15T18:49:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8dd21dd2f50115376d319238c636cc02df4906ef2fe6c9a074e6baddcd7a6050`
- PROD hash: `631522d7fbfbe68ccc8dde491cd1782c46a6e858b86856b6085aebee29d42d74`

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
