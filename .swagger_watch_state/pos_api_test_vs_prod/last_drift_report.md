# TEST vs PROD drift detected: POS API

- Time: 2026-04-25T06:59:07Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2313c2c5f468d5b261a8fd2188de63872ee94aa70771c7cfaef620e98f82ab2e`
- PROD hash: `b58fddc3537127ec700625672377c624943b6ce05af8c68bc4e40ab7bf15c723`

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
