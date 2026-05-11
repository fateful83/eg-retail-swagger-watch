# TEST vs PROD drift detected: POS API

- Time: 2026-05-11T01:46:38Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `033684a2785a941f0a8efbb2aa193c79fefbc97108ccbaa8e871eae610fc01da`
- PROD hash: `4bc18a98eda6513cb3461f6a112d2c5ff855d841a7c958a4ecd95278084dd716`

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
