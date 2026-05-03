# TEST vs PROD drift detected: POS API

- Time: 2026-05-03T07:42:15Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `71646f26e48a996661edf7a194d2994e088897deb93a7e164f58f852f9054c83`
- PROD hash: `f17358b36999a3606abfd59fb1eb3ca254541f406f7bff0e19e6f96d979fa00b`

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
