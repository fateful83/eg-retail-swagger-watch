# TEST vs PROD drift detected: POS API

- Time: 2026-06-05T01:58:20Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `379804ab26dd4c6a253440421fb383111c8edecc3a17bf23b48a848b65c88338`
- PROD hash: `3c1a120d3f6041448382879a1e2a11f1613372981895c8af1eeb68b5a801204e`

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
