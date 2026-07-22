# TEST vs PROD drift detected: POS API

- Time: 2026-07-22T13:14:49Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d9fedf908881036332bdbf7647c119fffa2000f7239e80b98cf84077314abc9e`
- PROD hash: `8dea97f3515aa0ffb9321d56d30a7cb8884f68c6fa4fb27237f06a8227721b8d`

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
