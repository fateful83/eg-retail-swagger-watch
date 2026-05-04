# TEST vs PROD drift detected: POS API

- Time: 2026-05-04T19:08:57Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f9a3e3c08403ebbfc99441cf03c4bbc4d4c7663ee7ae04883e6f5b041f1c551b`
- PROD hash: `5712dea8648a7df26f9694ade5fb4e68471e8dceea0b73f76760ead7de4bacc9`

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
