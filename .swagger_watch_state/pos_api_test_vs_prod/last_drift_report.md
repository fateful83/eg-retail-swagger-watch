# TEST vs PROD drift detected: POS API

- Time: 2026-07-20T08:30:52Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eb4aa17c8cf3b3e08e4e1ae0fd56e97377ec1e7dcb2d439359aef9be5c7716b7`
- PROD hash: `1d710901cdb5bd29dae51bd74c443d0f4e6b2ff03853652cf0e3744a62157aa3`

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
