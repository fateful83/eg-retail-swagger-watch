# TEST vs PROD drift detected: POS API

- Time: 2026-06-07T13:12:28Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e03c1c14382cc05e4db9e7950ca8affbe58d8e5e2ae0981171966eab5040a6ad`
- PROD hash: `aebfbf4a7166b12d31acc17599607984a6d66b36d6b98aa683996c3f5c905d38`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
