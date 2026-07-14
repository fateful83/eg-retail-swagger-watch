# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-14T12:57:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `71ddf7ad35151445cd3ab552c955ed0944aeeb9d7856350650cb2aa664eeba5b`
- PROD hash: `9086bbe885fd796305fcfeb156ba1fe378171e3205d35ce9e0065b7eda02ca9f`

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
