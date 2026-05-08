# TEST vs PROD drift detected: POS API

- Time: 2026-05-08T18:59:57Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0bcfdf80c86503d0c58132ee7e74a90e517e9db672a407a78efb5d9c155b31a2`
- PROD hash: `fd8359dee121e9f9dd93d5bb64e3d0f9ba2babbb4265ba9a942e9a40b2e8f1fd`

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
