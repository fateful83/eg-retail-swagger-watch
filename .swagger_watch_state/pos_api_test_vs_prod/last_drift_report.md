# TEST vs PROD drift detected: POS API

- Time: 2026-05-01T07:55:35Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `537b20dcfc4d4a157093a0197a97f02966b8ddb49000498331baa297b09daf56`
- PROD hash: `b6809b76d83e8ea47effa23e95c35e2beaaff01855d736412acdf553b4d22009`

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
