# TEST vs PROD drift detected: POS API

- Time: 2026-07-10T19:10:52Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `71583b32740b3935400805f87089f56c195d7f9b500f5e45710fd73f4900bb3c`
- PROD hash: `b6ca95cbd96dacba5a667e8cdf4ce4a825d4f76534c0a06bf9912fdae7835d04`

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
