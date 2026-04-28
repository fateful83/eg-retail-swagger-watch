# TEST vs PROD drift detected: POS API

- Time: 2026-04-28T07:59:29Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `07990f8d0f0c65077f24f00ae9087f56ccf94a4fe021d0ced7552f4b96a89fb5`
- PROD hash: `aeaf622bd75d86b8df3e7d518af4c20cebf84b86a9403048f9ffefd54bcde2cd`

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
