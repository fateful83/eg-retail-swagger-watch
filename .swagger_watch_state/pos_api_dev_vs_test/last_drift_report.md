# DEV vs TEST drift detected: POS API

- Time: 2026-07-07T01:31:04Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `aac8b828a59f46d6417dfc95ca4418e39e71ba64731144b64f6da964820a1588`
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
