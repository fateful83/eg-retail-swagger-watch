# DEV vs TEST drift detected: POS API

- Time: 2026-07-05T08:34:27Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `59a9ddb2e0237b78223ee7fffbe080c5f96a245d887e6cbc813f32c5883c27b2`
- TEST hash: `e92f2ea21ef74d75ec05fe444eb2847f1a7470c1b2eaea6f61e895260d1fbd4b`

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
