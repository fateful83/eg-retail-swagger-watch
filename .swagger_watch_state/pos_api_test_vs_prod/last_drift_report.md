# TEST vs PROD drift detected: POS API

- Time: 2026-04-20T18:45:53Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2b4e0a3d5d5ab6c2ce963f072a483132fdaae5a0ec4b902c8867861a8fcac3b7`
- PROD hash: `9b6441271716418dbf4121bff1428062073d4f62f8ca1fbfac74329d38928590`

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
