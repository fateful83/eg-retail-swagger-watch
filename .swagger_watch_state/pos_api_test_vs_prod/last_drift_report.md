# TEST vs PROD drift detected: POS API

- Time: 2026-04-24T07:22:52Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ebca6f6a45c0e138fd734d6f2ace3dbeb615120967d9578cd66ba2b640e4d42e`
- PROD hash: `586d5b92d953f80172f5013d9823d9dda9c13669f4efa620e65023d216ac2619`

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
