# TEST vs PROD drift detected: POS API

- Time: 2026-07-05T08:34:27Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e92f2ea21ef74d75ec05fe444eb2847f1a7470c1b2eaea6f61e895260d1fbd4b`
- PROD hash: `26e66c6138493f1df812c70afdfa4f0f9975e6f871dcde899031a4f1145f4695`

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
