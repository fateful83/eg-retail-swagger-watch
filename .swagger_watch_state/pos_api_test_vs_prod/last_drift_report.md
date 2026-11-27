# TEST vs PROD drift detected: POS API

- Time: 2026-11-27T01:11:17Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b0f2a4995d845e2be7a2d147453b70fc2ad4efe22ae6ee922917fddbac9d9887`
- PROD hash: `92fc37119084b87740e7e78c722da67c88011f79117f23fe12f8e1fc8791d98a`

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
