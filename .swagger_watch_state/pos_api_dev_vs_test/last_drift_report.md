# DEV vs TEST drift detected: POS API

- Time: 2026-07-14T12:57:46Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3f6953dcf5e6f72acb40d1e2b020ffe0e3d1dad9240c01d0ec31049000ec7b07`
- TEST hash: `f159bccd120718bfb3069b87c4eb8309530d134ccb1bbd96e34c7c0c9063dde2`

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
