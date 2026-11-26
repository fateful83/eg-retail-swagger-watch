# TEST vs PROD drift detected: POS API

- Time: 2026-11-26T01:12:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c9f04ff30f88daa453b9d07b004604c802014c60376d5becd002907b7dad43bd`
- PROD hash: `f05d6c4281c5db6ae835ce42dcb600e0655bc901248b97e0c387d4e3ee2d32cd`

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
