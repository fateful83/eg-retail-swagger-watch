# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-10T09:34:16Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `5266977b6860f8761e4b4ddced2ed8ab22cd5f7e6993ebae853bb289e57789c3`
- TEST hash: `5ab6cbf8b312d687059c2a4c0f5b469db1d9d5da02b8199a04b7e3349882d88f`

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
