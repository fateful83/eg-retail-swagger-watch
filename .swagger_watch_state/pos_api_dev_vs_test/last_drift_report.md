# DEV vs TEST drift detected: POS API

- Time: 2026-06-29T19:28:39Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3bcf5b8c70d7887e7a409e2570d1d724c67865e698bb45194c4eb1ea08fede72`
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
