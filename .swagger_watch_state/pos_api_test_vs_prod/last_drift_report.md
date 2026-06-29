# TEST vs PROD drift detected: POS API

- Time: 2026-06-29T15:22:14Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7059a8edf989b367d5976ad151d9cfe8363bcbed0bdc5b2b6503bfc4d3ef3d54`
- PROD hash: `239be91b0be06b3dbebea063d9f88455b32f5a0428324d6d414ac57fbbaa30bb`

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
