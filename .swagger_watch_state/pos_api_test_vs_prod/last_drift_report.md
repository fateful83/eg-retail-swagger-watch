# TEST vs PROD drift detected: POS API

- Time: 2026-06-28T18:57:39Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f702748905bc9e3a4c328185ccbc3fe116d82c6f6c4eabd6f97a357c007261c3`
- PROD hash: `0dbb994d28f2f614a71e928ffa6929fb041e72c5608068a226f4c3a49eef6470`

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
