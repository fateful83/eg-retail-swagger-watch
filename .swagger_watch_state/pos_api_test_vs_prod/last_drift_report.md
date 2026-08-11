# TEST vs PROD drift detected: POS API

- Time: 2026-08-11T00:41:07Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2add87718453cc7a410fa48e3a3af26716682eb562414fa0b32b852ad9553960`
- PROD hash: `687c24e4f95c2e57387b30b338a59277b31ae9bf8ac0a3ecaa296fa51a52187d`

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
