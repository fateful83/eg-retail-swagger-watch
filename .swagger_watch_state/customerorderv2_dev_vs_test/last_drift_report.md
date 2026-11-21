# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-21T13:46:03Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6b4b94f25c8aa1171cf68e2bb26906b51817c9533b1f839c5ba59965e9b23f3c`
- TEST hash: `99628eac39423eacb464a235733e56d0d2d1decec87ad0f72501edc9b2800b40`

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
