# DEV vs TEST drift detected: POS API

- Time: 2026-04-16T18:54:13Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `bc283a6e55ca02ea73febc463a127616812d7baa36d58fa1ab9bb0b2f975acab`
- TEST hash: `23f515982c023cfe2789bd8758e582b12707fc6a6bfea05f309d15fcaa30c321`

## Summary
- Only in DEV: 0
- Only in TEST: 1
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Different in DEV and TEST
- None
