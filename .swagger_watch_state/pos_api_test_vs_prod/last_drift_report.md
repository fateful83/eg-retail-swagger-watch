# TEST vs PROD drift detected: POS API

- Time: 2026-11-24T16:32:58Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `80d84427cfab638240192d1274dd1f026a6f5de350246037075c17f0bb0e4ce4`
- PROD hash: `516d16969fdbaf949483c3a8c98becfc4601e62b60d1a6fe83f273794f14d010`

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
