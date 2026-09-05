# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-05T09:30:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2b9286fba1ac0bfbd4e4f65341c7ecee35c060154cbab7223a7c0ef673a0c424`
- PROD hash: `ea64f2373850328a93507fb4856ee529e40b8952971f7509ebd318d91d3cae69`

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
