# TEST vs PROD drift detected: POS API

- Time: 2026-06-27T13:01:08Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `52e6f4c8baf04d3d3b2d9d1c50845ca977f54f9973013ba25870120b9413a25d`
- PROD hash: `4a900fdd44b357a016dd299d2bcf443f19cf4dcf5f01d3ea96a2675ca23708e0`

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
