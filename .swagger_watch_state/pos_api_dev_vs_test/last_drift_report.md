# DEV vs TEST drift detected: POS API

- Time: 2026-07-08T19:00:18Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7ee805e1caecc1844a0178cdc2dd924172f70d408bf767b8478cedff33ec5b8d`
- TEST hash: `f3477d01400b09a287ad12f8318d6e4ed4dfd0fed4e449b236a3bd879bff8b84`

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
