# DEV vs TEST drift detected: POS API

- Time: 2026-07-04T18:47:44Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7a3922c73d299395306a9578880c08edf566364da7c9bbb8d5391c798e4da177`
- TEST hash: `12e85cbc6f1655775e7f267a8d7b5b87361198880aa0b3c73cc2936d8bdfc1f4`

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
