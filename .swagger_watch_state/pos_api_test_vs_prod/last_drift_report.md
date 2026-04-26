# TEST vs PROD drift detected: POS API

- Time: 2026-04-26T01:17:29Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7b1ad881bcdc191e32962baf66c706407d331b6ab0556df831785a230509031b`
- PROD hash: `221f37cc7adff0986d2d1ccd39e00b5c40be6f9c7dde9eda0eed4165edc2769f`

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
