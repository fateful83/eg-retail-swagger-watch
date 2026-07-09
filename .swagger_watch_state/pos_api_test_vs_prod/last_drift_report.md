# TEST vs PROD drift detected: POS API

- Time: 2026-07-09T01:24:02Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4ace9be83db76fbd95e2ba90176a542cc33bd3ed29adc19b39d4289482374911`
- PROD hash: `9b4f16a901e0e6449fce0f82471fbcbe488af9f754627636e2c0153e74cca379`

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
