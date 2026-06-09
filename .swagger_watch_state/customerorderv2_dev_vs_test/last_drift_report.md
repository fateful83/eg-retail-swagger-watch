# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-09T19:50:50Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `cf44ecdd61ddbd6f6d4471e5260a668bbe44b536d769d99fccb28a9ac2355199`
- TEST hash: `803e154a905361a73e187fa128bf77d6135f6434e9adcfcfb1b70e101590afed`

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
