# TEST vs PROD drift detected: POS API

- Time: 2026-04-18T06:53:26Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8a706a34bc5a1e1dcdf26906c8718841bd4a2bbda07e52d40a45b2381041441f`
- PROD hash: `3d483ade69acbf16d8883217aa8773b7d13ab9f88514158bea660a9316ca22c1`

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
