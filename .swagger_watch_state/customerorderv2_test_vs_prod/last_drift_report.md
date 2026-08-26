# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-26T00:28:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7f9c935f4e4667c2a71059b24647d26053640f1aa1d4cb838589dae58ecfaa48`
- PROD hash: `9c698f105ff97372d705188ff933dc51d6657009d508c15e2d8f51f5f5629b9f`

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
