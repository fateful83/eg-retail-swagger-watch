# TEST vs PROD drift detected: POS API

- Time: 2026-08-06T08:09:23Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4060cf81235a9bcb6d54d584a3a289a8ad0355f438d5fd0d7c7c6d445556a9a6`
- PROD hash: `5c22594158dc9cb7a64a6fbfc527b8e87ac77886a0e5a9bb602dec703f19e5ac`

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
