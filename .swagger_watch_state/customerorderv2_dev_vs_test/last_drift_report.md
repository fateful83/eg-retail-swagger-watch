# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-20T14:26:26Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d012e3759038b114064386036b987ce2b4f83fd9604681b0a48c865eb198e403`
- TEST hash: `5f203d162d37de1778f647a9ddc6caf5be054c0ddcfbc577a32f2e969373b82a`

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
