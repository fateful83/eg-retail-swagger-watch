# TEST vs PROD drift detected: POS API

- Time: 2026-05-06T01:21:17Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dba456ccbd36d8f4534a8b94c1367fc17d50a8d1d3b7319433e8c2d02f4064cb`
- PROD hash: `de716e900c0b0b6dc4d5dd4fa378f45e5f2d8db340633f7b6fb3b22d216d4f93`

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
