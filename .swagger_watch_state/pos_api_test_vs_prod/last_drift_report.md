# TEST vs PROD drift detected: POS API

- Time: 2026-07-13T01:17:46Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `06d3de083cdb9dc8b5591a3897d3156cc25d4b9ed95d9432151f0b1ef6a514bd`
- PROD hash: `3f49d1e1b43104ca0d4b52d85383fb6ae98c6635d3a057a26034f66a7169b481`

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
