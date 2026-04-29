# TEST vs PROD drift detected: POS API

- Time: 2026-04-29T13:14:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `61448401801c04d350d2759418048e9eca869cfb02c000b2201938ac3de39969`
- PROD hash: `3c933dcd4818dcad76d5315757350acf3815197384f7b4e5d69eae276cce259e`

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
