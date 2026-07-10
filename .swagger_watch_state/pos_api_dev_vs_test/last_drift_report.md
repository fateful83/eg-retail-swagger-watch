# DEV vs TEST drift detected: POS API

- Time: 2026-07-10T01:21:04Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `ac3105de6677ecc9839500bb65ac460ec3c1e579924ae0d97dd720a9d0d568aa`
- TEST hash: `c1b4fb6db9dbab4d99d0e60bf3862a28a52838edab9f05540d2f0050b6c48805`

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
