# TEST vs PROD drift detected: POS API

- Time: 2026-04-26T18:32:41Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6d9e67f95da2ad97d6f5d2ebd43dd0a4d1485f481156534cfb41363915e6d22f`
- PROD hash: `51cbf46b57edf81c9e06f112ea58f428035a59a3777f74f760460280bad5fd8f`

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
