# DEV vs TEST drift detected: POS API

- Time: 2026-07-01T13:58:44Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `efa3a59e1f5c32ee2f5182311fa94fb0cc9b9039d21b5e5dd2c6ec76a1ec5dbd`
- TEST hash: `ee0e4042b9082cf79f530fd892217780c1584f9245a1b1f085465bbcc11de357`

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
