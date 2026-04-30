# TEST vs PROD drift detected: POS API

- Time: 2026-04-30T01:27:47Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `61448401801c04d350d2759418048e9eca869cfb02c000b2201938ac3de39969`
- PROD hash: `9466ebf21c930d7d83994bbc1f2dc22f884c67d72acf8e8dc1efee1ffff7f90d`

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
