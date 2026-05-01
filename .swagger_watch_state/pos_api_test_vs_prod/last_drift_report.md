# TEST vs PROD drift detected: POS API

- Time: 2026-05-01T01:30:03Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `12859b42365e38fdf03f87618a3c73aa51c2122c1f0ccae91af082daeda865d9`
- PROD hash: `dd41caf192c97170f304d2a210d9fe4568a30e1de9a5c14210edb4e800a78046`

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
