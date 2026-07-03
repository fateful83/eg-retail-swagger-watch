# TEST vs PROD drift detected: POS API

- Time: 2026-07-03T08:41:38Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `12e85cbc6f1655775e7f267a8d7b5b87361198880aa0b3c73cc2936d8bdfc1f4`
- PROD hash: `7ee51810d37137f7b4351b0c6ae4b79049dbddc8a7a0d428b81202490ea7577a`

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
