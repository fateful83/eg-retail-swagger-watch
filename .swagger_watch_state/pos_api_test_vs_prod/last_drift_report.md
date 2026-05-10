# TEST vs PROD drift detected: POS API

- Time: 2026-05-10T01:28:14Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c4df0fcd5af36da6f586fe707f9117a3064d65ccdee7f3df61bf01c3266d66b2`
- PROD hash: `9316550bcffa6d63847dfc9ea26806d7ee28d7b98df63b753c969d1b16df52ec`

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
