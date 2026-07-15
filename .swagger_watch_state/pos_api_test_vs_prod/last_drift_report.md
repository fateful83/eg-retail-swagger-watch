# TEST vs PROD drift detected: POS API

- Time: 2026-07-15T07:44:48Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `108f566296a8ad6079549bfe6ca0b891a3dcbdc25f0420c3a987d8a71c5d19d3`
- PROD hash: `7b9eeb20e9232a79ebd59545ed7910eea54745fda7023ca5231f5b4697108211`

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
