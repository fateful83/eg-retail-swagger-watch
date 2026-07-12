# DEV vs TEST drift detected: POS API

- Time: 2026-07-12T18:42:53Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `c2d266e58f7ca2491e5d6ba8d0c5b0ada1dab4546dae786032ecb6d8b02a4c19`
- TEST hash: `c1b3075597e8ad6cc76c4315f87f8a3fa0e4283283d4da139393200acc49fc28`

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
