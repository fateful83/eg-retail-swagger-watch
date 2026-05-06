# TEST vs PROD drift detected: POS API

- Time: 2026-05-06T13:22:29Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0fd14a47d737fc46ce5409850dac99a14ea49858597948da51287eb7e55e0493`
- PROD hash: `9409ff25a2956124cc328b1024b4cc9af9e2a5a9276e34270bc9eb47df84bd72`

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
