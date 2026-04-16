# TEST vs PROD drift detected: POS API

- Time: 2026-04-16T18:54:13Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `23f515982c023cfe2789bd8758e582b12707fc6a6bfea05f309d15fcaa30c321`
- PROD hash: `5d9a603264f95f6a9a2b6e511b22d24b1745e49b1bfd148837a7b235847fd7d3`

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
