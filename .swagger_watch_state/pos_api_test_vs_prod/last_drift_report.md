# TEST vs PROD drift detected: POS API

- Time: 2026-06-28T01:59:49Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6ac47374fc87860fbe2a7cbeda6a4996a85430e3b44a44c9d78a2c04f48546d1`
- PROD hash: `6268f7d25913cc23f9175bce44dc24aed9f89a3f4f87a13daf295f3f508463ad`

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
