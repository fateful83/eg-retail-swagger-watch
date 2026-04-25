# TEST vs PROD drift detected: POS API

- Time: 2026-04-25T01:08:59Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f056eeaebe2162acecded6db81c2d9c1f178a0cf0d07bc4b647ee01735f7b4b6`
- PROD hash: `a7d7dad1b28a1e430066377c7a93b9c20185856316f90cb42f04c75df71474fc`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Only in PROD
- None

## Different in TEST and PROD
- None
