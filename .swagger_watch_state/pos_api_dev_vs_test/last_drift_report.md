# DEV vs TEST drift detected: POS API

- Time: 2026-06-02T09:54:54Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3ae58cf60051a6419e93d7617995b8ed40c3918f8c52a68991f21bc913fb2754`
- TEST hash: `b23b17a5e27052594544a8c8fd96b3f7511a0766361c7c723e7fc2c6c736d521`

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
