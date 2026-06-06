# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-06T08:18:54Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `549e8fd51b922350233eb09c7864e7aea8736ce3da873841991b6955487b23de`
- TEST hash: `2820c3251ef3c0cd5422db0c2f2465e6d377bd7e432c16ff9caef232809eb4c8`

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
