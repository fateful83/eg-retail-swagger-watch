# DEV vs TEST drift detected: POS API

- Time: 2026-07-07T08:58:55Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9bb72216b9a8b8867e3b8c9b5934ead1b0b544b197975b742fc2338f42d0701c`
- TEST hash: `8e3e35e08bdbdf6c8e5bcf191cf51a9d18a8a339d20dafdd04530a13a7ef85e1`

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
