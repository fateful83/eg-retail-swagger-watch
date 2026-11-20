# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-20T23:26:39Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `2f92a90b0939f05b6322d477edafb79c27826795448f1755b843a717026858b8`
- TEST hash: `3250c09a5f01a511f944b9e6f57a73e2aca4192d2c890471086e236c9a51a2fe`

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
