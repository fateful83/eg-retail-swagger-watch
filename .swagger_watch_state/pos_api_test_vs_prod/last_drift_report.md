# TEST vs PROD drift detected: POS API

- Time: 2026-07-04T12:52:04Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2867dc82f50a91de58abdb9c7c80ce120771c07ea51220a7fcc492b54897a1e4`
- PROD hash: `42a15943bd11f8376ba845aa4a696e622989d73c1d71222d58ec403f5b7e9047`

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
