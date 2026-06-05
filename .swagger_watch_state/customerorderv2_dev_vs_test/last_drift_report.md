# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-05T19:25:08Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `b90e7405fa3398615a2a4245cc300e24c0430a2b23176b1ec01de4154e2204d6`
- TEST hash: `d40b10a4a211b60fbd1930a6ed5fdf8176244b7e859a4b5567db635832045c6f`

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
