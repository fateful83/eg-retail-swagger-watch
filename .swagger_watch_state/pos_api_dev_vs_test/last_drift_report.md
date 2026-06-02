# DEV vs TEST drift detected: POS API

- Time: 2026-06-02T20:31:36Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `ee54d447c919c9c9c621900f66bc2a3109845595530ddfe99ef49b11c3b0c87f`
- TEST hash: `47a5c38a11fdb4feeb14342c3323e9c2c427693bed4d986f63b7fef63c74897c`

## Summary
- Only in DEV: 0
- Only in TEST: 2
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Different in DEV and TEST
- None
