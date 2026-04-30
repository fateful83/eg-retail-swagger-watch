# TEST vs PROD drift detected: POS API

- Time: 2026-04-30T13:12:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9002620706090a44066129dd9a89bdee29fefb779c9cf8a49c31643d55a8164c`
- PROD hash: `a2ad3f90fca65cbdbecdc53c983c40f70ae5f2d8e3d44b3839f372ce62020adf`

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
