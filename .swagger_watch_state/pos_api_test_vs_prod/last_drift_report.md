# TEST vs PROD drift detected: POS API

- Time: 2026-07-16T13:09:34Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f324fe3ebc06b6d1193481a3debd55bb08966079e5364d0b6beb3a79624eb915`
- PROD hash: `6cca14fc1aca6975f2d7300d010f294ffd71bc00698346b4c44fec0edb5dff9e`

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
