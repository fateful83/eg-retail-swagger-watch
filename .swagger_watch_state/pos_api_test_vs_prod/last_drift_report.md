# TEST vs PROD drift detected: POS API

- Time: 2026-07-02T19:03:40Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b4c5a62d079a89ca3149784d3c015c9e495c189895b641edc22cbe1362931d4b`
- PROD hash: `1767fb04fc4e7b91fd03b9120d8412cd4c89c6d009f2c51e134b325799c3de2f`

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
