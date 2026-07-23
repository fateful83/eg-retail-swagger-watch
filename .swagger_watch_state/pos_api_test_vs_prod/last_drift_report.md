# TEST vs PROD drift detected: POS API

- Time: 2026-07-23T18:54:45Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `77df8ded668cf2dd571e562a07b9ebb1aab8ba34b072e8b1f5b2244c3046e142`
- PROD hash: `48559620e42884f88dd4294449d28769a8b4081c9522a1b5783181100c6e2be8`

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
