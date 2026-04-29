# TEST vs PROD drift detected: POS API

- Time: 2026-04-29T07:53:47Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a3d5bbee186fa7657db0d13b8bb47791c5da68cb6035360151fdd6ee8bd56d7d`
- PROD hash: `575f7743831498e0c7c529b06bca3977c2785dbe9caccf6ad7f80922b353e165`

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
