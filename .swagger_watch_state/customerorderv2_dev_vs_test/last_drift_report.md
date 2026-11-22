# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-22T22:53:08Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `cfcd1b9123cdff7ea2e361c4651b758c280072dd1dbc63c1ae3fc6725982049b`
- TEST hash: `307f11ed5c1d8451e53cbddddb2b95536347fe09eb753d1d09386e4939e6fa8b`

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
