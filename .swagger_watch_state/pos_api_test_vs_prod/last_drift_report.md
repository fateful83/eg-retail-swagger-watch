# TEST vs PROD drift detected: POS API

- Time: 2026-05-07T19:20:34Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1f03e1d5069cb75b7608b33fd3fad2c37ced670fab0031cecf4f98d089c6c087`
- PROD hash: `b4d4e76c01969961527fc2556011a159b77a930ec03346d4d6d0713feb63eccc`

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
