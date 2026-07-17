# TEST vs PROD drift detected: POS API

- Time: 2026-07-17T12:54:00Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `53a74033276aa9c889c4444d81f6398efc462383f8bc521cff7d13decb2c8db0`
- PROD hash: `3c3a60f5618b3a301d14c5181a2a3c329266ab1d2515b728b0a20307d534b82f`

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
