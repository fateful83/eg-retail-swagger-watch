# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-28T14:36:43Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `862cc0274eef3f244ba0726741d4047ab8b5e9a5a7bae7169fc2169b8771397d`
- TEST hash: `1a6cfb6d56b69c0a33884bafd5a09584bad4891722a733c54d040ba099ecd381`

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
