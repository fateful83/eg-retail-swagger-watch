# TEST vs PROD drift detected: POS API

- Time: 2026-06-26T01:56:43Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f96b5a3bdb78255c6aef9e6e056ee07ca5328864122da8b43050ac6d61f10894`
- PROD hash: `7a4f05e532cc0c947d0cf1c02dd5f587f1be6e23529a3df87da61e4a925a38b2`

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
