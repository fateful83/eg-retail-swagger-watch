# DEV vs TEST drift detected: POS API

- Time: 2026-07-10T13:47:24Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6b6126f5fea7c1d62581b0f1ad131a5352c18d25e4bf08152f9b7b13fb2d8952`
- TEST hash: `8b7b145e5e8fc161d352d734c31df8e16b2c3a0ea5836b7dac5557d176102510`

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
