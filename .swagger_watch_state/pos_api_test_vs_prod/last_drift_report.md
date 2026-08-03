# TEST vs PROD drift detected: POS API

- Time: 2026-08-03T19:12:34Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `268b1adf1d44c3b4ebbd33c9246e8d01edb02489aabcc5a8af018dafcbbbbdc3`
- PROD hash: `0eaadae133ce569a7bd51f0de52974f55cfe6fe424265861fd32608432e4096e`

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
