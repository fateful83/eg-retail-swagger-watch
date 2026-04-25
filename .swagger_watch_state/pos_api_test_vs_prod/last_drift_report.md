# TEST vs PROD drift detected: POS API

- Time: 2026-04-25T12:32:44Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2313c2c5f468d5b261a8fd2188de63872ee94aa70771c7cfaef620e98f82ab2e`
- PROD hash: `7c83948570edc44aa6c8cee004b47dd57bc02dc9e69c3fe700aa86e90defa775`

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
