# TEST vs PROD drift detected: POS API

- Time: 2026-05-02T12:38:31Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7bff13d2e662f3d48f74cdfa5909f92fae2621ba6501c3203283614f18ea320a`
- PROD hash: `3948a469e03144c1d862e69edef6bbaf354b1b8488aceb41ffc5c4a6cac16086`

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
