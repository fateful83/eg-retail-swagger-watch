# TEST vs PROD drift detected: POS API

- Time: 2026-05-08T07:11:44Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1f03e1d5069cb75b7608b33fd3fad2c37ced670fab0031cecf4f98d089c6c087`
- PROD hash: `f067a4afe3d310a4a9b9a85781d7d946c87ebb14146e75df7086954c28b39b34`

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
