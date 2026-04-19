# TEST vs PROD drift detected: POS API

- Time: 2026-04-19T01:14:46Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `21eb0bb9a0e2f61355ae798936e8bddb8d3151152af97d666b3615a7f4e92ee1`
- PROD hash: `edd5137cc74e5aee9b0a16e75f0413dcf479900367eb9ed4859847f77b887f51`

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
