# TEST vs PROD drift detected: POS API

- Time: 2026-07-26T18:48:19Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `592d777dff311a467f2fd664248ecadb84a22588e085f95cec558946d5c0ff87`
- PROD hash: `ae031c9344ec94e1cdc36ba55cf3d03a8428c2ec82cbf4a4318e620f0f72fdb4`

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
