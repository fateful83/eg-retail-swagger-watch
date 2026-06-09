# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-09T14:11:45Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6131e4d771cc4bd2b8fc1d3cddff4cc35bbbee76ded0109fc1235efe0d7fb5d1`
- TEST hash: `68937634f18d738659138b3072b3675fc5eacd9137d81a8a7c5c877b99f64160`

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
