# DEV vs TEST drift detected: POS API

- Time: 2026-07-08T13:20:25Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `06ffacf43f41b64b3682011ded07b1697ccaa3434562efe7d349099d56b6e5f6`
- TEST hash: `16a078a90ef2bfaaed3957fa2478bb4d3c6901e4f6f974a268a72c123d58a04d`

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
