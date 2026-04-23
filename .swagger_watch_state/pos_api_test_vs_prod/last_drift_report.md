# TEST vs PROD drift detected: POS API

- Time: 2026-04-23T07:17:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e612b3b7ea25c00d32e2804d63b11671002eb1ccba7bb1b446168a11946f39c6`
- PROD hash: `b8bac9d797c2e070e9b9aa003bca39df28479979aa54712eee15a4012d762620`

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
