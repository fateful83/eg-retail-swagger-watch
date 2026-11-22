# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-22T03:36:02Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `cea870c5231ef6acbdaaf1b6042d9cd6d65e57f90b3ca8ec6c0f8e08edf8f39d`
- TEST hash: `9d9b5a6e709e8dee081e34cea34986bd1875384d2dcc8c03e6b8fcd4e7417be5`

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
