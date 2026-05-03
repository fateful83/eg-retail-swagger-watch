# TEST vs PROD drift detected: POS API

- Time: 2026-05-03T18:39:08Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0384188243a68bff74744e7d7d7d5aabeeb79fdf2116e578a8a57225ebcd2d87`
- PROD hash: `17ac9f3bf7e275596b0894c9cfae2d8d2f8a5e67ecf0cf49dfb96bee554cd59c`

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
