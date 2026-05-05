# DEV vs TEST drift detected: POS API

- Time: 2026-05-05T01:23:21Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `da69dbd095414e684e9a3786fdad00d073c464a0a8b29a68bb1da78d29d18cb7`
- TEST hash: `1f171d569dba9f961aaeb26cbc6103608bafce05d32d4a8455649d147634eaac`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- POST /api/Payment/AddBonusPaymentToCart

## Only in TEST
- None

## Different in DEV and TEST
- None
