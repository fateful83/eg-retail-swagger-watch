# TEST vs PROD drift detected: POS API

- Time: 2026-07-18T18:40:48Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7b44f581809adc0305d8e49216b0cad09f198b7224579276aa67b158dee53cb7`
- PROD hash: `40161e97ebb10b870c5ec3bd0a69e4eea9bddde98c6fa0ea9105d5fcb4c8f4d9`

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
