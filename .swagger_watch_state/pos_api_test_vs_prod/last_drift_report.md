# TEST vs PROD drift detected: POS API

- Time: 2026-04-22T07:16:49Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `007154e02028dce10070a5e2315cb0ae685a0596dc2c2bd188e4fc8de4adfed2`
- PROD hash: `e1b99eb723e8e9bd7901ff389347780e9f9b816e8d91a4eb8bf18fa699527009`

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
