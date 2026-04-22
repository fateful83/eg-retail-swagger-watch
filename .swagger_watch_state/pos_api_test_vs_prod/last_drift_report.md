# TEST vs PROD drift detected: POS API

- Time: 2026-04-22T01:11:22Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2b7ba7dc55a17461bd17e2bd6e2368b79ed4f65a28953f0effa9adaea8661aae`
- PROD hash: `687e55caddaeb68dd8e1a27aa8d5d6acaadd4864edb009c1b95fdc825ade4a50`

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
