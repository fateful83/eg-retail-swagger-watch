# TEST vs PROD drift detected: POS API

- Time: 2026-04-27T01:19:18Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c9108de592044a2b6cdd4f1e580ebafad7fc3b8faaa45ac8d90b2fde26d7a2d6`
- PROD hash: `35296d8d3b62ac3f980acc0231fbf465d6123b879d398c7d45f2278ff9ab2601`

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
