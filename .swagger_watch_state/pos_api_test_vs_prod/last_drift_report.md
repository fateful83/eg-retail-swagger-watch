# TEST vs PROD drift detected: POS API

- Time: 2026-06-27T08:21:18Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b05dfdb6ef1ac9fd5f2228df2f56294b93b3594e4122771871308e700157c71e`
- PROD hash: `3dcc1693f44827e50034e522615e0ad4fdca4bedbe8d732b471308d06d5999cb`

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
