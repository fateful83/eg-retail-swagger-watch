# DEV vs TEST drift detected: POS API

- Time: 2026-07-01T02:01:09Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `319a189438ed236f52edecaceb41f46bab5043bef23fa14f4aea24b9606d5ccc`
- TEST hash: `5edf471c8a6ff0443692c32baffb5cf1b95cab3cb48f43da40030df3cf80ced9`

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
