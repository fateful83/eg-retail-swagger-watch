# TEST vs PROD drift detected: POS API

- Time: 2026-07-11T07:27:53Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cfecb419c8142f1f0f0d9aeb629c2362f7dd1d1c7280d39f1998e3aa0bee676c`
- PROD hash: `f95c1e00ebeec2bda5827c9f4ffd3477b84fb4b9bfca3fa9bb5844855af55eb5`

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
