# TEST vs PROD drift detected: POS API

- Time: 2026-04-19T18:29:27Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `23f515982c023cfe2789bd8758e582b12707fc6a6bfea05f309d15fcaa30c321`
- PROD hash: `363aaca75f90c408d8a3ac39065edeee1c5b27bdc9ed4e8ae6ae4552063a31c7`

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
