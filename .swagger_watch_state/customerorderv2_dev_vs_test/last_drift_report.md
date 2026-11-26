# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-26T01:12:45Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `12125f2ca1a5c594f43a3373f261a818cab2ae85e96985f161aff38bafd04c0f`
- TEST hash: `20d5612947517c1043481b63d0efccc8f1622e44dc705aa4f524dff8efc9b264`

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
