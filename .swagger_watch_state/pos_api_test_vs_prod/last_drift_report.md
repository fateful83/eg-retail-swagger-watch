# TEST vs PROD drift detected: POS API

- Time: 2026-07-28T13:23:01Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1d70e076e42761156efb480cfaf0ed5decd6bd047777e05dd0ec0c3464b230c6`
- PROD hash: `f0a7a6edd4617cb2bc9c6fec9198c16261507c75188ffa37ba1968c4f4153457`

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
