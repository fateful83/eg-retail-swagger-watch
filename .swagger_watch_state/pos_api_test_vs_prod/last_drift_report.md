# TEST vs PROD drift detected: POS API

- Time: 2026-04-23T12:52:51Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1c76800c5ead1ec84a59a9ceda7640cec7cfb88197902bb0aac8e6d9701b904d`
- PROD hash: `9d7a0f33a23eb4145ebab9487387914ab70cad11d4a90200270829fd42de2088`

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
