# TEST vs PROD drift detected: POS API

- Time: 2026-05-02T07:15:25Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f9007bfc412738f572d7bb7733d30f615b08c23d377efcfb13df190273444dac`
- PROD hash: `3f08e49d16514929972e37a3b608b1057d6ced7f5adaf54a56cda4470f9e2be8`

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
