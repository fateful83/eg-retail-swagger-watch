# DEV vs TEST drift detected: POS API

- Time: 2026-07-15T01:04:49Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7a455ce0452b58ac9189670685d54ad19dab51228fd84b97e0fe85ba69f0841f`
- TEST hash: `2c09e991e546a57ca45522e5e9c70533bd5c78da9ef5af8f704d08ec308bf8ba`

## Summary
- Only in DEV: 7
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Only in TEST
- None

## Different in DEV and TEST
- None
