# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-04T02:55:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e32f7caf9a3bf7f55b5c401610c3dac07bcd007022038866421204891d36a59a`
- PROD hash: `d0cb3a762f5879552e6077d041359afcfedc5d263b2f2fd156bb4d7bb3748f15`

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
