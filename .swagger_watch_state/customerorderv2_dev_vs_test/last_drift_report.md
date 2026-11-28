# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-28T00:44:54Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3146137345acae0d40fa0c23711cb971bb39bb4330c17e2554ede9fdcec5297d`
- TEST hash: `6cac279b29480042a066b0fb3552bcde66e18dce5d6e62c184616c4f69d6c033`

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
