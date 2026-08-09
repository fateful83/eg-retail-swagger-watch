# TEST vs PROD drift detected: POS API

- Time: 2026-08-09T18:20:07Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a1de88e2ac9889f2849f2c85ad0c23cdb21211fd6aabd882671c580aa3cf65d4`
- PROD hash: `aab6038c3e83262d8a9af9357489e81bc2e49fd061412f84b741f1e491e79827`

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
