# DEV vs TEST drift detected: POS API

- Time: 2026-06-02T15:49:36Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8316f35eb2390bfa22b2e55c65a4df525c07199114f409c5555cd0ca3eacd1da`
- TEST hash: `f85b545ee255b77004dcb68d85ef87edd5056b661c99d186d5fa8426d0a1aa15`

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
