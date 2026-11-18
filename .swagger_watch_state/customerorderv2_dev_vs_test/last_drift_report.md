# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-18T14:38:46Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8e535d31a43add35717591222e7ad09cb91ca7fd7e95065052f774023a1309e6`
- TEST hash: `0e971c6fc793c4674f3d71f92f88a0604d9d33b8107b4e0b13d3e87e4976765c`

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
