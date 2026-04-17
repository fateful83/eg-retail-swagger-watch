# TEST vs PROD drift detected: POS API

- Time: 2026-04-17T18:38:39Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `21eb0bb9a0e2f61355ae798936e8bddb8d3151152af97d666b3615a7f4e92ee1`
- PROD hash: `ffebced4a155e8ce6930af157731bad59eb29b7aac2e257c5fef3a484e497bd5`

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
