# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-22T13:40:22Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `cda311c278c3b4473f269b622539f856627e0f223c64d72dfa160dcc49ae3f7d`
- TEST hash: `82ee40c412f12d0a2700a5033616fb0dc4f2cc6e77c3073293c1244d9815d2f1`

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
