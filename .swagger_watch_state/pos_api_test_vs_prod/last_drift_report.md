# TEST vs PROD drift detected: POS API

- Time: 2026-07-04T18:47:44Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `12e85cbc6f1655775e7f267a8d7b5b87361198880aa0b3c73cc2936d8bdfc1f4`
- PROD hash: `495b8882699be94229a9d3a0e5ad41fc8a19b5d7170f5174d8556b048e1f41da`

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
