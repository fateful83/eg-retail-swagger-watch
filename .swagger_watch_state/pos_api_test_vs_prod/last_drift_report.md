# TEST vs PROD drift detected: POS API

- Time: 2026-06-09T14:11:53Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `40edf8640fc3c4ad7cfe5e50e9b5238fe251b098320408c42ae3adf43fa2a80f`
- PROD hash: `f20c0f6245f913523c1306d160072a855460458d1ed70d0480a133e40bc277ca`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
