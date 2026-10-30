# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-30T17:16:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cc6657ff4da9fd73dd12921517e3150efabcf97b729eca193017c5c39d19c819`
- PROD hash: `da04fd3d889d2d2902558b0f21e9dbf74530eeee536c9b1301a04e1b31bfc814`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
