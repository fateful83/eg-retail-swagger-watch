# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-21T22:29:24Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `bd0fba41b54439aceaeb98afc51d81c6ea8c52fcd69b715ba8f72d23964b8561`
- TEST hash: `870cd7e57e230035796b87fdbd4c6777b4ba5a2c3f9d2cde0c8f91486e298a02`

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
