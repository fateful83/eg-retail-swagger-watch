# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-08T10:09:10Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `58f9e0ee0cf47b843ec4c9fb4165d916728df152884a2df70d0379a998a01e8f`
- TEST hash: `6a696a7b33d63f8b567f0c9f3f0c980c768c5b549662580f1a87eb5e89f004b7`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- None
