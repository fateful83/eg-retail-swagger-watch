# DEV vs TEST drift detected: POS API

- Time: 2026-07-09T14:20:33Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `e8b2bb541130c13bbdae84602b9b0b889a117d74d9e67c8c38f9e57c372ab785`
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
