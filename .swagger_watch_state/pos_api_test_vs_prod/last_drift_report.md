# TEST vs PROD drift detected: POS API

- Time: 2026-05-02T01:20:58Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f9007bfc412738f572d7bb7733d30f615b08c23d377efcfb13df190273444dac`
- PROD hash: `73ebbb2f4c4248e0de4cdc9bbec2cf855cb522c4f7ade79608486f7d7a0692a7`

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
