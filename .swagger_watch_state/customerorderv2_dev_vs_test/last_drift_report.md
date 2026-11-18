# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-18T23:38:47Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `46772d1310a1270ee9ae0367856ee154369ff89e6dd4227749af7a9376f5a815`
- TEST hash: `8b42d3cf731c5370f6a7ae644b54d18d7fc6a1097490d31201010136bd8ed564`

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
