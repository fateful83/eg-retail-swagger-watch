# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-23T10:20:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3dcd501ceb736bd3db36272d69a0022e55be34e3fe64dfa906f33f20709d351e`
- PROD hash: `cb269622a999f5ba8d1527303892b8c2736756a8e286f796e201aef79c1df88f`

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
