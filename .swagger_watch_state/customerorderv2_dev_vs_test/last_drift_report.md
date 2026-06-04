# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-04T02:13:29Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d08703daaa96220078d5811cd773f4716dcad4c8d16a855b444649f69c78566d`
- TEST hash: `b4c54a8455d35f06f96017e5e198da62da0c39b6b1c566f363b6e243ad9c2110`

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
