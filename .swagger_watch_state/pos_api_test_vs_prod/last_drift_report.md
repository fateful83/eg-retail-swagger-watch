# TEST vs PROD drift detected: POS API

- Time: 2026-07-26T01:20:20Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bcf25d75205d03b2ba27c67d6ec2882289529fddd82c7eac356230989476bb73`
- PROD hash: `1e014ae13eef84cb1c1fb9329edee921428e462810e5bcb7650f71ff9b194da5`

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
