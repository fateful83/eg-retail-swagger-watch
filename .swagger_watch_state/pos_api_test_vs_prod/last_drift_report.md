# TEST vs PROD drift detected: POS API

- Time: 2026-06-07T08:40:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `94ca3790071bdcfd935f7b6b60ec746922f4a3f3f5d5e4857801c5aa275baf20`
- PROD hash: `7e83e4a1ee65c0cba0c3164ec5402f56097c857c49b78bb301a0629fc98d8342`

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
