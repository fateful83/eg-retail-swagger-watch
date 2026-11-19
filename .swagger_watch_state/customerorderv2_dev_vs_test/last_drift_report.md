# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-19T04:37:29Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `b7f1a46eabce5722162ea9379387e86f6326423572e8c52600e703b33196d7ea`
- TEST hash: `da9f579989e1dfaad1df9fa613dea47d88796a0fe0122a6a9908fb4bb8588f4b`

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
