# TEST vs PROD drift detected: POS API

- Time: 2026-11-25T16:13:08Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cf9cb8dcb8db5cb6fcbc016575612899e806003ce911405fc0226893f86aa901`
- PROD hash: `4f79b64e45c20870ca8e5e0ef5c46fedb50c79873a896dd21681a6deb6d89124`

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
