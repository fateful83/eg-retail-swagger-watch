# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-09T08:53:29Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `b1617f3410eac9c090b26b8e2fe51c829be10e50264eafccc248920e16fae2ba`
- TEST hash: `b18a953e141e5a6481df21343eb5100aa1677e3624cacced570876e78a2d4578`

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
