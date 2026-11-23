# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-23T04:08:59Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `ca693d8c3ede251d2bb9d262f5d39ed0847342bc9362f99e4757745c87898b2d`
- TEST hash: `2f75bfac938af9f976627177a670a24182d05b69dccf5c4b55fddacee40c18b8`

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
