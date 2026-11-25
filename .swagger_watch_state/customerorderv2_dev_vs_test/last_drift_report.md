# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-25T01:39:26Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d4bd20f16ac5c52c00e5eb825ebda6749c91ea8e63e790c146afe9315811660e`
- TEST hash: `f22bb27b85a1f7efbb38ef938a006730a426c59f6775b3f7fe744cd861b420d9`

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
