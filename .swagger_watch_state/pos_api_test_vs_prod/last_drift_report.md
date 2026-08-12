# TEST vs PROD drift detected: POS API

- Time: 2026-08-12T07:02:41Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ca95801e62968e62da791ee8033e9f188e8f945bcad7f155560480a1c0bb3a39`
- PROD hash: `b21717f83d4ea48b94435d4828ad0380e8d5f4c94b53c912f5a0426796f1999d`

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
