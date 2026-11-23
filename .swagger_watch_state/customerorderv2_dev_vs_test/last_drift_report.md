# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-23T16:34:21Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `f71276bfd1f5788ab5a2d76290a4871088df8b2f93f9a8ce4ff8cd14f8c4267a`
- TEST hash: `927a80eec2b931eb7c4006cb0cf5670ff5460a92cdc918e2c0552bfe828d1017`

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
