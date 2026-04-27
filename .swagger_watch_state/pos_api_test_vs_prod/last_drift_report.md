# TEST vs PROD drift detected: POS API

- Time: 2026-04-27T07:59:34Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8b80f499c47553fb6afe85070ecc4210d8586166729492ca5165b4a212e1214d`
- PROD hash: `cbf7171b90a9252b4e866970bb9e586f63ced32bde05ad9e01d332c07f8401bd`

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
