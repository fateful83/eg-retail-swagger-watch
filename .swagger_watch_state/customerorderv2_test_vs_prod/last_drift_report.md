# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-04T15:11:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8f60b5feda0a3634824d23b4e8b7147c47f99252cf1936b30549390dec94cb41`
- PROD hash: `96897a5b379521e71a5a13bc54f898b3de21523d7b4e8d860cd957d8b85dbe5f`

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
