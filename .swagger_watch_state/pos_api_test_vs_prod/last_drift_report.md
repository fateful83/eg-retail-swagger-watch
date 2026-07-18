# TEST vs PROD drift detected: POS API

- Time: 2026-07-18T12:42:03Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b87d0f09b2fa027236dc8c7f0079bba0abe322b018bf1ad4418fcc9669d8630`
- PROD hash: `f978c57cc0fe5150c6eb2561b787341e6b2acaded79f12680aa2d38ccd3a0011`

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
