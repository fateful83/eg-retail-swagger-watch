# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-19T17:48:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `223e41565cbf5d0007b2c0093cdc4bd93c29825d85eb714e609583231a904da3`
- PROD hash: `7d896aeb84fae08504ae9f37006f2a265d748a39d2c5f871b9f8478292447ff1`

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
