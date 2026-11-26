# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-26T15:52:36Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7a76fb68ecfcf3aa9a3cbda3bbb357842b5ddb903dc17974ac7543f178b67329`
- TEST hash: `87f0ce95a806d7200632e3e6fff30c1e5308165d9c7a64b83542521558d1d355`

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
