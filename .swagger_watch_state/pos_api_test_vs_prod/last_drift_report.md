# TEST vs PROD drift detected: POS API

- Time: 2026-05-07T08:08:19Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0fd14a47d737fc46ce5409850dac99a14ea49858597948da51287eb7e55e0493`
- PROD hash: `835bdc6f575ec44b3a116bf919889468a0072eb2ef6f07e575fbe5585673e71a`

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
