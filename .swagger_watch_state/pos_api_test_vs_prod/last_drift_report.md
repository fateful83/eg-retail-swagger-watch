# TEST vs PROD drift detected: POS API

- Time: 2026-07-20T01:17:56Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eb4aa17c8cf3b3e08e4e1ae0fd56e97377ec1e7dcb2d439359aef9be5c7716b7`
- PROD hash: `51d3e6c3fd480254a6f007cea6519e9cf7200d37386e08ca96279d614ff4608a`

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
