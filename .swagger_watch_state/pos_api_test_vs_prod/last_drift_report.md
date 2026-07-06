# TEST vs PROD drift detected: POS API

- Time: 2026-07-06T01:31:07Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1c6bbee6a15432938e57453bc63722ba360185c92d9d8bc9c34a5a681cbc6b27`
- PROD hash: `9d05921f7aa10813423320f2c5e02e1ec4d96ed52b57beb344001e40f865dc5b`

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
