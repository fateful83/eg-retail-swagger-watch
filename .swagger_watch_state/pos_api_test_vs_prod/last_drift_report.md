# TEST vs PROD drift detected: POS API

- Time: 2026-07-05T01:29:55Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ddcf013e42a6bf88bf845df8c1dafa5edb800744298520076d7317a8f86eb4bc`
- PROD hash: `b0091e6c47b49c93682e01ab15564af2634c1ebcaf5f05b2aecc4d183e3db3de`

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
