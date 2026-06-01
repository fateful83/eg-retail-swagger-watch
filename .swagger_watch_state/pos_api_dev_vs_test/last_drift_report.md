# DEV vs TEST drift detected: POS API

- Time: 2026-06-01T02:07:18Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8b968e8ebf27e4e761db98a9cfa5d62f62da1ec0e77d2005ef7bb38668f714f9`
- TEST hash: `1bdd33741329e203e5786ed3bc03b1612165210222806ce56be108c6e119951a`

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
