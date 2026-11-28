# TEST vs PROD drift detected: POS API

- Time: 2026-11-28T00:45:03Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `45703b7d17d370fd7875b74a7828f31a292db983cf7fcd991d2dc578a28a4cf9`
- PROD hash: `5af40932cbb7013dd77aec333c1a3f4b71f7ee04246ee418f9742aa9fa06f55d`

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
