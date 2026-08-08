# TEST vs PROD drift detected: POS API

- Time: 2026-08-08T00:37:09Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b8fd4538cded61797d0adfd7dd47db5d965a73b6a8efeac8c616a978e86e6beb`
- PROD hash: `949e1f006b8202b87fc1f4a94486516d342f2826c4438b5888155e3ef5b88d73`

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
