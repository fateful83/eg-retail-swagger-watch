# TEST vs PROD drift detected: POS API

- Time: 2026-07-12T18:42:53Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c1b3075597e8ad6cc76c4315f87f8a3fa0e4283283d4da139393200acc49fc28`
- PROD hash: `bee2e14593e43507b34674e66ae3d7910ba85efd46d76d4544204a9a00a1b597`

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
