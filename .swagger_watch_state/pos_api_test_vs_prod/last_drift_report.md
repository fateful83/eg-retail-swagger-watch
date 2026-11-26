# TEST vs PROD drift detected: POS API

- Time: 2026-11-26T15:52:48Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `34a64b4fda8f38522d8fcda95298bf26ccb774925fa9134f7987cf85f0112223`
- PROD hash: `cc21d448cb76205106a132996fdb26f662194738bab393d356d3798d70f4d09d`

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
