# TEST vs PROD drift detected: POS API

- Time: 2026-08-05T08:10:45Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a388b649bc5262a18f6b4370d5f233ba71c8cd6bc86e138f42c62d07ad1b14f9`
- PROD hash: `751acd318b29ccffae7f3701bfb897be29c46931ca455ac172805eb8ba5455da`

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
