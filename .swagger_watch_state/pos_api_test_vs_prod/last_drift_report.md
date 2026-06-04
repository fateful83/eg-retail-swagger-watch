# TEST vs PROD drift detected: POS API

- Time: 2026-06-04T02:13:55Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `359e5fea50f8b1ff286afabf64fe2c13ce0846e1be9b690f8715648b5c86c7a3`
- PROD hash: `949c78ee2cc473a45ba216346293b14e7cdcdf514b31642ef4e89eb8442e9587`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
