# DEV vs TEST drift detected: POS API

- Time: 2026-07-11T01:15:20Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `cade82bdb0b3f9dabb481b784bb0a62ebf7f866e706818d0c33c8b8c3b8e8564`
- TEST hash: `fcb4d56cc7c378cbae50765eb8d30f75210e37b92811a955d571853a6ea8679d`

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
