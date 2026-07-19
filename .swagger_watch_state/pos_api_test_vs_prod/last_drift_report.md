# TEST vs PROD drift detected: POS API

- Time: 2026-07-19T18:43:38Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b87d0f09b2fa027236dc8c7f0079bba0abe322b018bf1ad4418fcc9669d8630`
- PROD hash: `2e53ec28ee2e23caec6b230b898652ef3c8f8360144d94ffefc1259307b9f3b7`

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
