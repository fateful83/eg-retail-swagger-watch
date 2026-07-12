# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-12T12:45:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `625cc1a8da49d223ec5993d51c80c6a4c177c96023fe789d37219806d8a20a97`
- PROD hash: `31d281e0c7a90bf2f207ad565c87be01fc3dbd8b6fdebd05f1861f3701381f56`

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
