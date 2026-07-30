# TEST vs PROD drift detected: POS API

- Time: 2026-07-30T08:01:28Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4bb5ac8b8a010d6b4c1de38691273e0bd1c1446846eae3ce76d177480344c617`
- PROD hash: `999e62888b665f1b6144e7b5df52ce7c8c8974105ea15e90fdea7c7b86da151a`

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
