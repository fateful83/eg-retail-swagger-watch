# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-07T08:40:44Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `e7d3a72876582214fc2fbc7c2aab7a08ac1dfbc4e30ae5c94c697ffd26ca626a`
- TEST hash: `70d959a95a98160925cdd277e0f7c6483547eea5bb591c819a4c81ba52fe5a63`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/order-status

## Only in TEST
- None

## Different in DEV and TEST
- None
