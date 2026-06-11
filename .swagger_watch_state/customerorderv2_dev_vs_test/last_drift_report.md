# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-11T02:08:10Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `16e79da9927bd1bec07a55abecb6765fa7cdc11449c0fb27b32f71891de18782`
- TEST hash: `b637a9df89a41f5cb0e909b7d769f420bb0a35e94211b8aeb0231ab6e78920a4`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
