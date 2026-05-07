# TEST vs PROD drift detected: POS API

- Time: 2026-05-07T13:21:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c109a27ba8ec2802c36b5925b3cea42cfdb7505bc4ca0f94701d58935f2bd0dd`
- PROD hash: `211812a58f09c74dac17ff3ad6a02ebd1f3a0c7802f7d06e12507b76022b86e0`

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
