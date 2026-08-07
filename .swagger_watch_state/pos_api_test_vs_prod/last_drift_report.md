# TEST vs PROD drift detected: POS API

- Time: 2026-08-07T18:35:16Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `03477dd5883ae7e744efb3779a68ee774dcd900b72c4f01ee95c85d3c4157233`
- PROD hash: `37271d79f9ee531db771a4998bbabde57bae3bb49ef5f761037704659b76a9a1`

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
