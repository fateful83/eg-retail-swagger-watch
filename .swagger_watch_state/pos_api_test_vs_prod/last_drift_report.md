# TEST vs PROD drift detected: POS API

- Time: 2026-07-02T08:37:08Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d7c2bb8c7b7c4ca49603e4ad6c7255e20305f87955f45acf539f8e77e666f2e8`
- PROD hash: `d49c8382cb07a516c9b47c0fab6bdf7021d174b4a2c969c3d5f9b6296b031ddb`

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
