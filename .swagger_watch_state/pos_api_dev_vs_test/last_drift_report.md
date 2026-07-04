# DEV vs TEST drift detected: POS API

- Time: 2026-07-04T01:24:04Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `5388644fcfc395925f4e1a7de516cff47f9eab912795920b5a25f06be6f39bd7`
- TEST hash: `f7289d253e0490d31aa2e4648168d89280df1e3ee329ef2def4afeaa4c5fc918`

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
