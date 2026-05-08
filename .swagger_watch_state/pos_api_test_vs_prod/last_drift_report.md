# TEST vs PROD drift detected: POS API

- Time: 2026-05-08T01:29:35Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dbabd00f023b7016bacbc4ab56550032972543dd866b6e9b86b425da7de1b59a`
- PROD hash: `36bf4960df62a3ed442ad4f998990405f33f6c8f5e229a01904176dc502444ca`

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
