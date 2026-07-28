# TEST vs PROD drift detected: POS API

- Time: 2026-07-28T01:12:16Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1d70e076e42761156efb480cfaf0ed5decd6bd047777e05dd0ec0c3464b230c6`
- PROD hash: `b3c7f9d9d9eb0421b0994ef67575cbec32752a034b658a897be9255c45447d7d`

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
