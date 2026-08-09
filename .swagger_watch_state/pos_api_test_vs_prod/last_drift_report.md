# TEST vs PROD drift detected: POS API

- Time: 2026-08-09T00:39:19Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e8c8e79003d42945fae3262a5a0f8c0b758151a891bbc77c3141e35ec74d0858`
- PROD hash: `2254b3926ff8af70035dec23d4ebbea9156dd597610f0bfaccf257491da969c1`

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
