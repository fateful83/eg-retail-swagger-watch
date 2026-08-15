# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-15T12:10:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b5e7a70bebe3dcd143931878f1fe13ec5bf87ff940917bd35b15824dd53eb168`
- PROD hash: `de00db1e7a91c112844fac885c7b47176063eb0352fb93dda82cc09f6da4bc3b`

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
