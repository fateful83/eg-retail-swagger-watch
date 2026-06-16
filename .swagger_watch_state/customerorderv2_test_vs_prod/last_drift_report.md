# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-16T20:33:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fd3d5b9151ca273c719c0ccca4dba265878fd558cd5b72408593af9cde54c951`
- PROD hash: `be8610e99db4892e46ec88586a1fd3967e4302ade5b3ef7c007e73d1121a838a`

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
