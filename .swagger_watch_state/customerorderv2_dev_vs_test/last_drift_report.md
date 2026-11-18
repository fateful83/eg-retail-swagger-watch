# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-18T00:04:33Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `37694fd08c41e5cf29caaac3583b97660243b2f667c7fe6357b74e06797ec1bf`
- TEST hash: `d61483add4a45be80474fa39ff5b2172582e230133d1f9120fac28760dd13ef9`

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
