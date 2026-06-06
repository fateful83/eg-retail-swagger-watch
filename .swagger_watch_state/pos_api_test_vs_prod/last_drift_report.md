# TEST vs PROD drift detected: POS API

- Time: 2026-06-06T08:19:02Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d6a4a8bab707e2560d52a9c6c6f11edde4b97f85b0064ba9430be751607268bc`
- PROD hash: `ce55e09c90f96554781b796aa87a3471219dd84c74477c4a4e3d57774779104e`

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
