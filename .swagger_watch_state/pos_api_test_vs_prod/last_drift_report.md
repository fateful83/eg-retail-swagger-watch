# TEST vs PROD drift detected: POS API

- Time: 2026-05-02T18:38:11Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `71646f26e48a996661edf7a194d2994e088897deb93a7e164f58f852f9054c83`
- PROD hash: `5b1c6f3d3f89936e312a0cfc51838f0f5f2eb961fe0ee2430eb72811e4da3835`

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
