# TEST vs PROD drift detected: POS API

- Time: 2026-04-30T19:02:01Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `12859b42365e38fdf03f87618a3c73aa51c2122c1f0ccae91af082daeda865d9`
- PROD hash: `733873efb95cfcc3a5a26bb94610cd595c4028d29f237d7e95c58695bf6c6374`

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
