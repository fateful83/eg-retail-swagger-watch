# TEST vs PROD drift detected: POS API

- Time: 2026-05-06T19:15:45Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0fd14a47d737fc46ce5409850dac99a14ea49858597948da51287eb7e55e0493`
- PROD hash: `8fc8f40c0a36d0869d2aad1f79a0147da64d03e3760bee998b24101d8c3d885c`

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
