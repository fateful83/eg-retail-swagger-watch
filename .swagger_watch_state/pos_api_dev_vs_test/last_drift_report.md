# DEV vs TEST drift detected: POS API

- Time: 2026-07-08T08:02:03Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `06ffacf43f41b64b3682011ded07b1697ccaa3434562efe7d349099d56b6e5f6`
- TEST hash: `10cf61562bd07832b6a9f3f7957132d5b5be74654672355bb2037614fa30301e`

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
