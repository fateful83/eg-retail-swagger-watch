# TEST vs PROD drift detected: POS API

- Time: 2026-07-01T13:58:44Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ee0e4042b9082cf79f530fd892217780c1584f9245a1b1f085465bbcc11de357`
- PROD hash: `a5e86d91a3d1d8b1239cd50cbde13eadc3f9cef913164aa061da477708aeacaa`

## Summary
- Only in TEST: 0
- Only in PROD: 7
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Different in TEST and PROD
- None
