# DEV vs TEST drift detected: POS API

- Time: 2026-06-02T02:08:40Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3ae58cf60051a6419e93d7617995b8ed40c3918f8c52a68991f21bc913fb2754`
- TEST hash: `c480f3c0bbe882b8dbda1b9f39873f66c15bc7dab6c0cf83dfe1a55d3c1a309d`

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
