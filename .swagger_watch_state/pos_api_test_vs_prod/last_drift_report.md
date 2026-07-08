# TEST vs PROD drift detected: POS API

- Time: 2026-07-08T19:00:18Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f3477d01400b09a287ad12f8318d6e4ed4dfd0fed4e449b236a3bd879bff8b84`
- PROD hash: `8ace35dc883c4010e89ef26b53876f6866a959be6bb0d41bdb39e2445863646f`

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
