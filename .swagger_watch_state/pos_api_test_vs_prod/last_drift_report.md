# TEST vs PROD drift detected: POS API

- Time: 2026-07-22T01:15:55Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4ef41793b2828714e772f2ec9132f995c60fc4b7eccf73a8621f641a9924597`
- PROD hash: `1e5d71b44eb1560566ed0ddf9c49f4a19aa6b82936e90b72b248ea380cbd79df`

## Summary
- Only in TEST: 0
- Only in PROD: 7
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Different in TEST and PROD
- None
