# TEST vs PROD drift detected: POS API

- Time: 2026-07-19T12:42:46Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c150e528675e9e1e144c0dab85a819c42015288d3339240c30ce06525187ddb4`
- PROD hash: `74f9a6e865146cffa878de1fdc4f81eca7b7fb3e6311eb15447cd73ecc9fb2a8`

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
