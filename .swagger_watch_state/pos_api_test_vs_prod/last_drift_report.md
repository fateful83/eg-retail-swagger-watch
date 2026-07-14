# TEST vs PROD drift detected: POS API

- Time: 2026-07-14T12:57:47Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f159bccd120718bfb3069b87c4eb8309530d134ccb1bbd96e34c7c0c9063dde2`
- PROD hash: `53ed23ce4f40d4af66bdadf0f6cdea7d3b62396bddb501422b12e02b975f2eab`

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
