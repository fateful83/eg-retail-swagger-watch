# TEST vs PROD drift detected: POS API

- Time: 2026-05-01T18:51:58Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `537b20dcfc4d4a157093a0197a97f02966b8ddb49000498331baa297b09daf56`
- PROD hash: `971657085521b19f7ffbcd66852a6e177cc971b517a859693d8f343d26f663fc`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Only in PROD
- None

## Different in TEST and PROD
- None
