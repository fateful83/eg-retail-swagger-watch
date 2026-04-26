# TEST vs PROD drift detected: POS API

- Time: 2026-04-26T12:34:25Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `25efc4bdedc19e6b9cc8710493549d1d5a7e17c0c6064a0df47265b3cb159899`
- PROD hash: `8630f3abba249553582a0c65126993b99a631931eda441c45c743bb0e158b722`

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
