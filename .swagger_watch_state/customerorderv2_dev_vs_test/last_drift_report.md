# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-19T23:56:54Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `90635d0efc04274a9cad2d81d9d94b40b82eff6946c05e099ecf79025a88d62c`
- TEST hash: `e652614439a7116339d130720783e8079695bebae2b7e0e5fde156de8ecf1631`

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
