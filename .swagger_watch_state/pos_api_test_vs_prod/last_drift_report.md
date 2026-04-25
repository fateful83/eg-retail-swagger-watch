# TEST vs PROD drift detected: POS API

- Time: 2026-04-25T18:31:30Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `615cb0b4b5dc2ebbfdb23a38f88a411b37710d572932c78ddf39864a929f25df`
- PROD hash: `5b1ff1b0d40c81035db2ca3df2a3cff2ed18a2006d49980879ef22796fb0face`

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
