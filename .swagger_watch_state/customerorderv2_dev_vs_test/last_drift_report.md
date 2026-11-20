# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-20T04:33:32Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `969ab12946e29946e07ac3f97a629b194e3116ac9cf6dd5a0614334e900d0276`
- TEST hash: `828dc7756452ca1254f09ef83b01a747a3e46bcd91297a434512e3818c01a067`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- POST /api/gateway/Orders/search

## Only in TEST
- None

## Different in DEV and TEST
- GET /api/gateway/Orders
