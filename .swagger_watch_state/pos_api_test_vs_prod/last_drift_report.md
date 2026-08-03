# TEST vs PROD drift detected: POS API

- Time: 2026-08-03T08:53:17Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c4f647d0081822f1e337d412566ef8c1ea1ad51642ec89d376a6e2361149f072`
- PROD hash: `840329853d0078bee718db287dfc32d6b0b7ccec78c97a6c22c4c25e8ee23d97`

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
