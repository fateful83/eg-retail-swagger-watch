# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-13T10:41:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b7174f2992a891641be874acbd0d867945b5973280b4bb407d2a79404c402529`
- PROD hash: `dfc873608d251cf7ca49f1c6e8c7869b8d8437ef59c94c70a29e13df360626cc`

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
