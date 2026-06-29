# TEST vs PROD drift detected: POS API

- Time: 2026-06-29T10:15:14Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7059a8edf989b367d5976ad151d9cfe8363bcbed0bdc5b2b6503bfc4d3ef3d54`
- PROD hash: `4e970eb22ee5d652a8a91801034ca837d1ac36d905e0ad9e78f184ddbdd3cd19`

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
