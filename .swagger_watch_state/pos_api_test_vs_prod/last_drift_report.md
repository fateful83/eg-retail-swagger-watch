# TEST vs PROD drift detected: POS API

- Time: 2026-07-03T13:25:36Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6a362c39ba98db8728fbd68ed69de5f501e16f2dbab58db7b22049b749d93d87`
- PROD hash: `6e892a28427dbc0b4f81457f010cdf9e4a9b7aac7c9a348fa40a7e8d43134f49`

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
