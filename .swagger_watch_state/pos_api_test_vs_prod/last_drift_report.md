# TEST vs PROD drift detected: POS API

- Time: 2026-05-07T01:27:22Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c109a27ba8ec2802c36b5925b3cea42cfdb7505bc4ca0f94701d58935f2bd0dd`
- PROD hash: `0c58a4320077d95e57a794e541e35f2bccce2d389b8707a4a064f85c2caf8b50`

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
