# TEST vs PROD drift detected: POS API

- Time: 2026-07-15T18:49:46Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `55575fbf05f852c1384c41eb8c4bdd22578436a1ba1ec07a2fcfc68126576160`
- PROD hash: `f1d2ba360696ddc23123cb95378525c6904c24764f10aa522f460800d03c54c2`

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
