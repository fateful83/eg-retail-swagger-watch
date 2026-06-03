# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-03T20:43:28Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `c66d6b40a26fe71fbed620d8d9a02bb3b5fe508b61fc51047d1f8112aefaee73`
- TEST hash: `0dd1a0629d073c3c25eb42128727f85975ed77320908d341e73f51722cdc73cc`

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
