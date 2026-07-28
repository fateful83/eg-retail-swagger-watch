# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-28T13:22:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5adf57f8c7e9301599bacd3ae2d2ded9b6ce556122a1cfd389f19a131150858d`
- PROD hash: `57532df9305580461e66f9e9b9f66260715a6f12a9e442ed9b5236ea2edb1acf`

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
