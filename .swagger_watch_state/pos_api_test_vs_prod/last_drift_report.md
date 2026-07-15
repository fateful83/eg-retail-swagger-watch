# TEST vs PROD drift detected: POS API

- Time: 2026-07-15T01:04:49Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2c09e991e546a57ca45522e5e9c70533bd5c78da9ef5af8f704d08ec308bf8ba`
- PROD hash: `1e76651819e7ce16d44d040a1a0536519d5890e3cc6657af6ccda61190777c56`

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
