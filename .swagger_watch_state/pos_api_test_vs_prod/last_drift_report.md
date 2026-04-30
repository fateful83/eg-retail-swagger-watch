# TEST vs PROD drift detected: POS API

- Time: 2026-04-30T07:56:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `74ea6161ba8f77ad0127d48bf0fbd3c7eea3483f1e8a9408161de8c0a5a3faa3`
- PROD hash: `21806dededc37badd166a6708dc6041a52c96fd1689d6a382ce5f7cc3ae71519`

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
