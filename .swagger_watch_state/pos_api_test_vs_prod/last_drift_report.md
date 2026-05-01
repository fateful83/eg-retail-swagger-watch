# TEST vs PROD drift detected: POS API

- Time: 2026-05-01T12:46:12Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f9007bfc412738f572d7bb7733d30f615b08c23d377efcfb13df190273444dac`
- PROD hash: `5fad3ed1af8be3294e632d70fab6f47cd9b3fe3cf3d9d6cbfb5888d9125154eb`

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
