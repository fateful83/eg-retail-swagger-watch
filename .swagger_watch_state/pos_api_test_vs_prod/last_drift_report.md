# TEST vs PROD drift detected: POS API

- Time: 2026-07-02T01:54:54Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f40da4db42ba1fa51e8152671f6f822c5dcfca1536e2f4b101fd4ac3e2696c2d`
- PROD hash: `2ac9dbeeeb9420f2220605f11d7a5b862665617ebbd769166f98114c6eaf49e5`

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
