# TEST vs PROD drift detected: POS API

- Time: 2026-04-28T01:25:43Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `07990f8d0f0c65077f24f00ae9087f56ccf94a4fe021d0ced7552f4b96a89fb5`
- PROD hash: `575d4bf39a45afbdafa6d423fc860bf9ce67f923d7ed9b768c757ecf3e1704a0`

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
