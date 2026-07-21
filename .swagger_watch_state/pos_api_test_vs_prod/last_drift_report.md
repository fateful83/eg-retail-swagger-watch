# TEST vs PROD drift detected: POS API

- Time: 2026-07-21T18:59:29Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4ef41793b2828714e772f2ec9132f995c60fc4b7eccf73a8621f641a9924597`
- PROD hash: `5b319d7551b93017b4f5dceb210457ac527593c1e02ab40c94d9f5968e7268fb`

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
