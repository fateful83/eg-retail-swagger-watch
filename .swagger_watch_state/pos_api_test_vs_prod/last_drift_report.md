# TEST vs PROD drift detected: POS API

- Time: 2026-06-03T02:16:16Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `47a5c38a11fdb4feeb14342c3323e9c2c427693bed4d986f63b7fef63c74897c`
- PROD hash: `be105589e7896362e30071d90f445527571cdec097945fb8da0b69b532114351`

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
