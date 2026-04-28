# TEST vs PROD drift detected: POS API

- Time: 2026-04-28T19:13:35Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ee98d025b5ece75f391633efa62fcdfa200fa9a5eb64f20dbc9d72f38d3a4720`
- PROD hash: `b3f6849a71a3935448266217972b437a83fb0069bf9426314824d0aea984efac`

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
