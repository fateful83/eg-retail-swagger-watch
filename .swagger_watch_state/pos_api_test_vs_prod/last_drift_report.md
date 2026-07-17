# TEST vs PROD drift detected: POS API

- Time: 2026-07-17T18:46:49Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `53a74033276aa9c889c4444d81f6398efc462383f8bc521cff7d13decb2c8db0`
- PROD hash: `4390d79d36ddda8bb278fb8470adaf4f53eb15da357de25e56f1cf6ea09eade9`

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
