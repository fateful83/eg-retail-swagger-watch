# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-30T13:47:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7afe53bddd17f31fcfe900a918f849888ee5cfad04455c483d0b6034169941eb`
- PROD hash: `d19d26571f79ec27d3dde2b0a8f6f4c943c7e5f2ad54201737ba868e1ce0f488`

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
