# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-24T03:30:04Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8d4c5cfa764983156e46d5ad71f2f7e4807473951d041db6413656f87634129d`
- TEST hash: `03521c3a9b354553b79437e4f246efdaa22704a391e9f06d0821ba820388052f`

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
