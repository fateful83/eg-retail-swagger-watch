# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-24T16:32:47Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `29f3451e4ce2ab2650b68654446e07d6f86ae5cd28f39c0b6408049acc9fb066`
- TEST hash: `408617e135d413d2fad3789150357243618be80d3b3a5a937f8f16210d840f4d`

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
