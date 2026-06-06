# TEST vs PROD drift detected: POS API

- Time: 2026-06-06T18:59:46Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `62de0ddf5ee527c88be92acefaf9c18e242396fea78e462f325014bac7ada334`
- PROD hash: `49083b8fc69b3da8c0e7fe9c946f92fd48042aa694543b536b5ed50ee2b26119`

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
