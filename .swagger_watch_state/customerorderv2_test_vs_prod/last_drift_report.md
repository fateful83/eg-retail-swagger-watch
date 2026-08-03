# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-03T19:12:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f0b141510b082792463a1d08aceb686f4367619734768ee72245de9f3ca447be`
- PROD hash: `2334512137b9f4856802ac11b0b98e03f2375efa54996704d9c2191bf5c5f366`

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
