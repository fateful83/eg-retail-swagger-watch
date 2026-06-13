# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-13T08:41:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `65f4f58467fa0b3f66398033f236899645f61dc63aeb3dc76060073e37fcd1b2`
- PROD hash: `1184fda147c2db400dce99f7f49567a85f26aca421cbc2af99ef39d4b1a7d824`

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
