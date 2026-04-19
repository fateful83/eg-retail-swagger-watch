# DEV vs TEST drift detected: POS API

- Time: 2026-04-19T01:14:46Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `64435dd8c4b14871d2d68f86aa2ed002dc52e4be13ab2938231144b39b8a1fb0`
- TEST hash: `21eb0bb9a0e2f61355ae798936e8bddb8d3151152af97d666b3615a7f4e92ee1`

## Summary
- Only in DEV: 0
- Only in TEST: 1
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Different in DEV and TEST
- None
