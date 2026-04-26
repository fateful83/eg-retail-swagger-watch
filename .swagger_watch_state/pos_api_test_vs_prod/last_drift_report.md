# TEST vs PROD drift detected: POS API

- Time: 2026-04-26T07:13:24Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e6c094804b105c93025b0bf402c7ee4f47a00c786400d22016beaf01ffe8b2a1`
- PROD hash: `a270f63cb31810f1a41d76e6207c5b2f2e19b83ce5887a12e7a18ceefde18a19`

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
