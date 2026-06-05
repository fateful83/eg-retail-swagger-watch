# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-05T08:58:40Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `e4c07c81457dbb0ca4287b3a9a9130672fb7a9193cf57c5e2bb6aa08150495cf`
- TEST hash: `797854ecab12aca49e7d19c91fb9c865d1c44820d9007eda8b66c00378eaf328`

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
