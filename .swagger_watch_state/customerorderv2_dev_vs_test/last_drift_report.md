# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-07T19:00:35Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `bd62b3b2fa4e1ae347008004213e8c3db8ca53ae69afaa965353f1e4c9aea4e3`
- TEST hash: `c7cf197968a5441c9a22df48c5d7d6117761ef05c2c3e1ed780313a268cbc768`

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
