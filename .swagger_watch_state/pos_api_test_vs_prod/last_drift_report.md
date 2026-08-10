# TEST vs PROD drift detected: POS API

- Time: 2026-08-10T07:01:14Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `47ac1ac47d7b51b741f0ae69754290b51c36faa21052c43832dce6d31684705f`
- PROD hash: `2da59dcf2f6629448c68c5b62a5f7851ecc1f71188a4f8f6f9c223f4b85796e9`

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
