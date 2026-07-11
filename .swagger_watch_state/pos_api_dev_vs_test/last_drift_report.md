# DEV vs TEST drift detected: POS API

- Time: 2026-07-11T12:43:30Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8026a39600b5d9ad06cf222fe320d9eae84ea5fc905803a019d15f461a9a3953`
- TEST hash: `cfecb419c8142f1f0f0d9aeb629c2362f7dd1d1c7280d39f1998e3aa0bee676c`

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
