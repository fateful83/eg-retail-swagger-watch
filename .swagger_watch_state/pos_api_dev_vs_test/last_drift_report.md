# DEV vs TEST drift detected: POS API

- Time: 2026-04-19T18:29:27Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `a988376e5cc23089d2ca561c87d4bf522b7440319ff3aaee933cdb0f4f244ed0`
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
