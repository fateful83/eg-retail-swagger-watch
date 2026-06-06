# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-06T13:00:06Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `b2c990cc2381d450bb02bb191aeba9e862a2e4d5aedde729e2dd887c8a741525`
- TEST hash: `ca3f1d426a379066eafa067a3450198cfedefe52a0bf2edbc00042087f3130fa`

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
