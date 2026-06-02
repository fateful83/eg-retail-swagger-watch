# TEST vs PROD drift detected: POS API

- Time: 2026-06-02T20:31:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `47a5c38a11fdb4feeb14342c3323e9c2c427693bed4d986f63b7fef63c74897c`
- PROD hash: `d5a8db152928aaec0ad595a8cbfdf33da1c3bed283879cc12510c83d1eab89a6`

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
