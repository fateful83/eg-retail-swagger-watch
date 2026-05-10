# TEST vs PROD drift detected: POS API

- Time: 2026-05-10T07:50:23Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b920f9adb458590c73d4daa6fad09884ff7f47c29c2104aac130b28f8f7b683e`
- PROD hash: `cfaca70fc93ae7e53ffdaeee8fdaaa3162e626fad5a96505cf4068c6d9c7ec06`

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
