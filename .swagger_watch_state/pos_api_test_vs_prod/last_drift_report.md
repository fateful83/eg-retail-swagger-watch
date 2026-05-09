# TEST vs PROD drift detected: POS API

- Time: 2026-05-09T01:26:41Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0bcfdf80c86503d0c58132ee7e74a90e517e9db672a407a78efb5d9c155b31a2`
- PROD hash: `8328553c816504ad89ec97ee0b046d42c160f0a6ae3a725ce5f281e184346773`

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
