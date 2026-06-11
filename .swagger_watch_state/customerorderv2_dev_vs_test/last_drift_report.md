# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-11T09:56:53Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `60202c27cbbd9a83cd319e5112386cfb6217048274a3a8241f3af1e98e4dab1a`
- TEST hash: `c81fcc9124fc92df6db5a2c7d8ab328f74e648345acaac50746d62ce8c3381fd`

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
