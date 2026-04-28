# TEST vs PROD drift detected: POS API

- Time: 2026-04-28T13:23:31Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cfabaac92a179a1a143b585b046f4abdd4627ecd9f31f5614e8e865316435077`
- PROD hash: `9e8590ce4ce7c49574dc2577ca3b684d600dca11547ce0b3f99f7bb7af3d2253`

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
