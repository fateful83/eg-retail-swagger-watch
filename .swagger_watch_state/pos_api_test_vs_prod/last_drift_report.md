# TEST vs PROD drift detected: POS API

- Time: 2026-04-27T13:11:05Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5728ece3eceac6f56b528b2caa3e701fe362f361d8cbe80dddba5de66e89a4bb`
- PROD hash: `9e6719f9c6bca176350b4eaf9df88839a634e59c4f514a3c7381206fa45d28b6`

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
