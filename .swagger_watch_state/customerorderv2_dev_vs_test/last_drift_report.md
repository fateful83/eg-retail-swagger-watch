# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-21T04:22:19Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `1bb1470e648c068a9089c67bc952adb006d04f86a367e8b8f9babc0c61a4b26a`
- TEST hash: `beaa96a0b1056add591bab01b2b98512cede996b78a227a97a8263ba1d5978b2`

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
