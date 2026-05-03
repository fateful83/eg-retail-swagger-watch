# TEST vs PROD drift detected: POS API

- Time: 2026-05-03T01:24:09Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7bff13d2e662f3d48f74cdfa5909f92fae2621ba6501c3203283614f18ea320a`
- PROD hash: `bd2d37ae70cc2e1c2949e1fee23b2cac2fc9eb5d7141b6acc8c55cdd09f3d6d7`

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
