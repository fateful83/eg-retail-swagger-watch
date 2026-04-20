# TEST vs PROD drift detected: POS API

- Time: 2026-04-20T12:57:47Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `05c9374d6aeacd65560c75622b57a09a7f57680297d7a8ce86780d3daedbcc16`
- PROD hash: `1e9bf2bfe5d87c3cb970b6378c382de08355ec040fda1c72d00b8ed7f47c198b`

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
