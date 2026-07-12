# TEST vs PROD drift detected: POS API

- Time: 2026-07-12T12:45:13Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9559ff8ef2df598edb2568efa6aa02eb13523da8e297e7f138e3e1807895c770`
- PROD hash: `baaa235554c72a940afbc9e1a1e8a6bf9c8de78da04599ac0e4993f7051e25e9`

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
