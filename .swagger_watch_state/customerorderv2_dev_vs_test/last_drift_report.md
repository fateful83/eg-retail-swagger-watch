# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-03T16:07:57Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6bec249c1e569d023d0d7129045b84cc848ca0b32a7318372aa8be60d4889f3f`
- TEST hash: `7c1038cbd41d2de32802ce96aa3778de6317455d298930a5e77543f219619d7c`

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
