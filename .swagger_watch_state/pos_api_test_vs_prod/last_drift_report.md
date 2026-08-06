# TEST vs PROD drift detected: POS API

- Time: 2026-08-06T01:11:42Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b5f0701fc93dd27044558d8bdc4685e729e39c512c5272365e426721f903a48d`
- PROD hash: `7c8f7cfc6356d224a6ac3282e78f9ec6d7f065bd3e4d1bb99e7f926a71376712`

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
