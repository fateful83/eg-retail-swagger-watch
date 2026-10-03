# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-03T20:16:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9ca9c67abbe466055eac024d325205b7868450c8f5b0709c56f5fd3977b2fd5c`
- PROD hash: `3e1c7f179e9192bff078816f2d7d6be2d40fbca39b99d70038322751316d74bf`

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
