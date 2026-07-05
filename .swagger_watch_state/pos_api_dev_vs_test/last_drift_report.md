# DEV vs TEST drift detected: POS API

- Time: 2026-07-05T01:29:55Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `434bf894c1514ba7c0ec2fe6b03bf62364252d0a2dd6b972c32d2b04b445b463`
- TEST hash: `ddcf013e42a6bf88bf845df8c1dafa5edb800744298520076d7317a8f86eb4bc`

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
