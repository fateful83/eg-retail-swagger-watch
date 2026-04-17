# TEST vs PROD drift detected: POS API

- Time: 2026-04-17T07:15:29Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8a706a34bc5a1e1dcdf26906c8718841bd4a2bbda07e52d40a45b2381041441f`
- PROD hash: `3c6fe252fb777ab030138954f18613f0336d1c7d7525be23189f74dee1ff6624`

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
