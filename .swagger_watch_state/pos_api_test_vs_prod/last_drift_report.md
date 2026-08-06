# TEST vs PROD drift detected: POS API

- Time: 2026-08-06T13:26:31Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b5f0701fc93dd27044558d8bdc4685e729e39c512c5272365e426721f903a48d`
- PROD hash: `de37fbf588ed35fd8c40d8ca0bba4b57d5e040d77ecd4c8a1c94a7eccec9fcdd`

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
