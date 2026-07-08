# TEST vs PROD drift detected: POS API

- Time: 2026-07-08T01:16:07Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `639de72922a1669656367a7d00bd53364e4c0d9211c04eb2f599b2361bfedeae`
- PROD hash: `f4f830dfc8664c36ce843e29e3d0d28d7fbd18f20dd4ab8b50b9f05dacaf7043`

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
