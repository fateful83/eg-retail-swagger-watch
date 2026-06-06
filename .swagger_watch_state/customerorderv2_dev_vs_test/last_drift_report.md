# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-06T18:59:35Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9cb023b2d69d212ff1f41b23c4c2857cfb805d2cec0a67150523ccceceee9ca7`
- TEST hash: `86da452906de2fdb61f768f203b33f26a62591e7d5fba791303aa9a28a0dad74`

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
