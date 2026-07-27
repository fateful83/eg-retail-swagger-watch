# TEST vs PROD drift detected: POS API

- Time: 2026-07-27T19:05:32Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `25c3e7671dd68c65efa553f7f59a3683875376e0872a6b19d2753bece069b2ca`
- PROD hash: `6b65b6ebbd2afa080c309e9e218fd93a2a8c06655f38451b93decfe7d146c408`

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
