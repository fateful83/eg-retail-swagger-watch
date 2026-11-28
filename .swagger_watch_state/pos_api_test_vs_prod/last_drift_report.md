# TEST vs PROD drift detected: POS API

- Time: 2026-11-28T14:36:52Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4c848faa0744ffbd9510447ff853bc56221143bdac32766ea66ec4e3e33c59cc`
- PROD hash: `66356a3e6765ea2dcd347d2ab86daa2fbfd9f71d22410b2dee8c82614cb1b9f3`

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
