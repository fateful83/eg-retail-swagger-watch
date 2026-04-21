# TEST vs PROD drift detected: POS API

- Time: 2026-04-21T18:51:54Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b9965271f01d70770232618b35b8a6c15aea092e0258bc7a807a61ed710b97c6`
- PROD hash: `38aff2601d5093113e2691bae919741a9b5d7c740f5c42b9695e34ae741aaa35`

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
