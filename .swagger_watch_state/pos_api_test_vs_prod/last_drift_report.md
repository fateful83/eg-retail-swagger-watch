# TEST vs PROD drift detected: POS API

- Time: 2026-07-28T08:08:10Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3d3765b76f478a237bc388c1b427ca67b3f6b5011c9c9a7a1abfce5e08e6f6c5`
- PROD hash: `0ad321ffd1d7546066fdb5ad08bd81651246b45f7598c3f6f24c73967445abda`

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
