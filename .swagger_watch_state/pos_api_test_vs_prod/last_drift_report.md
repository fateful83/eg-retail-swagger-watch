# TEST vs PROD drift detected: POS API

- Time: 2026-07-04T08:15:55Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7289d253e0490d31aa2e4648168d89280df1e3ee329ef2def4afeaa4c5fc918`
- PROD hash: `2690486452fd373e3874c43a9f0b2d9b4ae732f9f1336650eceb6a62fe77d74f`

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
