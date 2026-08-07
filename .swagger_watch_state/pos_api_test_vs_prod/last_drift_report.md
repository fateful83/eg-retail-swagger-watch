# TEST vs PROD drift detected: POS API

- Time: 2026-08-07T12:33:12Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b8fd4538cded61797d0adfd7dd47db5d965a73b6a8efeac8c616a978e86e6beb`
- PROD hash: `14bb917a8f57d243ecd0b4d78fc34a3071a1537ce729f2ac2ff4f0775525f18a`

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
