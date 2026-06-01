# TEST vs PROD drift detected: POS API

- Time: 2026-06-01T02:07:18Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1bdd33741329e203e5786ed3bc03b1612165210222806ce56be108c6e119951a`
- PROD hash: `7d2961ee176d2967e3a8b0d16dd171b4cb3b146d866a5514d562b24b7876cfed`

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
