# TEST vs PROD drift detected: POS API

- Time: 2026-07-14T01:07:28Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b78afa16a3a814fd1a76b191664c9cfca7ea9f16002bb274239a58dab9405c69`
- PROD hash: `0b360d31a4232b1f11f6123bd4a34f57a3859627d231b4472049834bef56e3f8`

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
