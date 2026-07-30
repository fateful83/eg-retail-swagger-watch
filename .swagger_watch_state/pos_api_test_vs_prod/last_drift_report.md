# TEST vs PROD drift detected: POS API

- Time: 2026-07-30T01:08:10Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4bb5ac8b8a010d6b4c1de38691273e0bd1c1446846eae3ce76d177480344c617`
- PROD hash: `643ce3324be2ae23bd7cb6fe70e862b40acc48c1f55eb7a67b6b8a3ef1b87727`

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
