# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-07T18:35:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f6fa4f312d077a0a6f16c41399865a3f8d1624ae6beda4398acd0abcdbe8cad1`
- PROD hash: `309fd0e02c883e1d7f32e01a7f4aafbe1205195d04ae381812045954db4fdb95`

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
