# TEST vs PROD drift detected: POS API

- Time: 2026-07-15T13:01:10Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8d4ff3404918b93558ab8946ba5ebb05c84a5f50b37d216a3f2a179418bd7030`
- PROD hash: `17956e7d3149523849cc3bc5b3a0b05abde0bd9bd4c614868a6fc1b95862f99d`

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
