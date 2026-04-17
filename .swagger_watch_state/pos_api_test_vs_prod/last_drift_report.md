# TEST vs PROD drift detected: POS API

- Time: 2026-04-17T12:46:45Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `23f515982c023cfe2789bd8758e582b12707fc6a6bfea05f309d15fcaa30c321`
- PROD hash: `364b087f8d68bbd6f700c07d92fa53dcb7ae1bda22c26cb34862d01e47bb0a13`

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
