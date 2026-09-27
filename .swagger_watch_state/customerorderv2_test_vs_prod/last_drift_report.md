# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-27T10:53:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d8f415e45a3f85a0dd007914edd0f7809ee06df725ea53d3e20dfc582f4b3089`
- PROD hash: `60b683f304448b0a0fc10f03c0a539e3d1c2b5b231e60a681e098a8a8ef001f5`

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
