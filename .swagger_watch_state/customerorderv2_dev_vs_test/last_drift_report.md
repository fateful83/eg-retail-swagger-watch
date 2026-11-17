# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-17T14:57:41Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d597f17fac47bd38e43b53786e7e23efa82ebe9e95848c1ca4833b3637aa3858`
- TEST hash: `8c05887c52330a35fa5bf7aa2c6bc9af43bb206917a824ba6f656578ec4ecbf9`

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
