# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-03T10:26:31Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `011c5c73f71b549fc5cd20f8d579326b2c029f147763cb984446bb76e06d483f`
- TEST hash: `0c6f323e86e367c092ff48c9acb9b8d1f68d9d3bd73d2cd51787e6638f910101`

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
