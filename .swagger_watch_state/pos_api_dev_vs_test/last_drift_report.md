# DEV vs TEST drift detected: POS API

- Time: 2026-07-13T08:38:36Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `df7ba3e31ec206cec409d1c01a78df9ec7810f1ae699e2c2b5ee158564d36fbb`
- TEST hash: `cb2872195f1f065d7504f9633d1e550516f276575b8df860d75ad42c13e46c14`

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
