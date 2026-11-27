# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-27T01:11:06Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `11feac78dba705b4f8f3bdd12ffa8924dfe4974008e569632a280d942dde8049`
- TEST hash: `5d4c7951994f19ad0edd64fe2278c59282d3ca8fd3e63831ff406789a3fa57bb`

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
