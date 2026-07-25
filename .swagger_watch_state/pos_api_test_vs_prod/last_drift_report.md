# TEST vs PROD drift detected: POS API

- Time: 2026-07-25T12:53:00Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `798088afc7d00f7c521c3aedd9bd436b08f557e1f1bd980f3e50c953590d8036`
- PROD hash: `9541d61e95211da5736ae3ecdb5b8e16ff563dd84354d2e8303abd2636c8ddee`

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
