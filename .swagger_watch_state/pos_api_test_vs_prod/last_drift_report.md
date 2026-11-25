# TEST vs PROD drift detected: POS API

- Time: 2026-11-25T01:39:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2310cafeb350a923159d11006074645b1a508c62c9efeab007004ad673758124`
- PROD hash: `901a7285bfe09ff970869123f47249fa04f5b848d56e68f8ab693752b5be5371`

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
