# TEST vs PROD drift detected: POS API

- Time: 2026-04-18T12:31:13Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `21eb0bb9a0e2f61355ae798936e8bddb8d3151152af97d666b3615a7f4e92ee1`
- PROD hash: `7e9b2a2157d832660a0f7513877b994181aa97fd89de245448f11a02537725e3`

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
