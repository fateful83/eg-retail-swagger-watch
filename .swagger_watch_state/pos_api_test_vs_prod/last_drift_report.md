# TEST vs PROD drift detected: POS API

- Time: 2026-07-10T01:21:04Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c1b4fb6db9dbab4d99d0e60bf3862a28a52838edab9f05540d2f0050b6c48805`
- PROD hash: `470941614c1e439fc4e694f56fa8c4b3bb2ef99cc9daa00fe544a93eeff1cbc7`

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
