# TEST vs PROD drift detected: POS API

- Time: 2026-07-08T13:20:25Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `16a078a90ef2bfaaed3957fa2478bb4d3c6901e4f6f974a268a72c123d58a04d`
- PROD hash: `5c4da9382d0aa2d7e48e3bbd256737f3f57543b51c766b8b0c1fe8ead866ccc0`

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
