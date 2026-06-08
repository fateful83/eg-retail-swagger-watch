# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-08T19:55:11Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `798ba23e9c20cd8d02913a6b5eda3470af431c3b89619f4fefab8ae85bea194d`
- TEST hash: `5d77c86a8e3c650f6cc427e50e059c28125ebf3e02900fa2b80a936632cc43cd`

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
