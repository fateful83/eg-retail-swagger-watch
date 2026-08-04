# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-04T13:29:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b3ef24508e054d33431d79b444beae766a4d2d8fd1ef080ba20eeb9c1c151c95`
- PROD hash: `a071e25c504cd204c1908280122cb5377561ddf6c54c5d1b59d6b24b54e0cdaa`

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
