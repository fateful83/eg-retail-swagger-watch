# TEST vs PROD drift detected: POS API

- Time: 2026-11-27T15:41:34Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7d800c20bb3b7cd20cd0f558720769191536153f676153288ae8a2bcee7f388`
- PROD hash: `f35fff8a18851ce388c7e4070ecd9b8bf3ccc847004550b70a3f50dfe650eb6e`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/ReceiptOnHold/CountOnHoldReceipts

## Only in PROD
- None

## Different in TEST and PROD
- None
