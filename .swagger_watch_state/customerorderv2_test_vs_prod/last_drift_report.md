# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-17T02:10:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `728625ef2d975d719dcdb936069f201b8566318e39d585db7c7206703dcfe0b3`
- PROD hash: `994e3358f8db9fae970a0dc9769bf618e7ca62d588392bdf89415a5cff97d753`

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
