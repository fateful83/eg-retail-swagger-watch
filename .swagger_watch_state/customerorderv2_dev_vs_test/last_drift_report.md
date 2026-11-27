# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-27T15:41:20Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `78ebace3882146d47d9bbd33ef76102515ed8196a328b9349f60fc59f3d1c0ce`
- TEST hash: `7e48ffe4240a291d349b53b82250f55ed578b609aed40d3a5ab5cf2ea5a5d3d0`

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
