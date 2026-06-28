# DEV vs TEST drift detected: POS API

- Time: 2026-06-28T18:57:39Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `412ab40f3e3c8b40667228915890f9eae8fa786796cdbe78f1f302e49834c0b8`
- TEST hash: `f702748905bc9e3a4c328185ccbc3fe116d82c6f6c4eabd6f97a357c007261c3`

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
