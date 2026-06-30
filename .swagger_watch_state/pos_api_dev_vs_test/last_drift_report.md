# DEV vs TEST drift detected: POS API

- Time: 2026-06-30T01:55:39Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3bcf5b8c70d7887e7a409e2570d1d724c67865e698bb45194c4eb1ea08fede72`
- TEST hash: `40ecad92c28965cc24efef726cca0a2b2492534f1f29a3d78a4937917e56b318`

## Summary
- Only in DEV: 7
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Only in TEST
- None

## Different in DEV and TEST
- None
