# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-07T10:47:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dc076093e7d3e0d82c2c3785cc73dc64140aa20745298582562c209d7f525558`
- PROD hash: `2949baf9549274039835597d7c8d40058aab8a231c49cbf2bf75a4c9344decd7`

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
