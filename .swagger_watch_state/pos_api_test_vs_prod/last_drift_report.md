# TEST vs PROD drift detected: POS API

- Time: 2026-06-06T01:49:56Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d6a4a8bab707e2560d52a9c6c6f11edde4b97f85b0064ba9430be751607268bc`
- PROD hash: `5e398c5e887393a84f53bd2d5611d73741aaf6a7a4f3ca8e493372311869a3e4`

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
