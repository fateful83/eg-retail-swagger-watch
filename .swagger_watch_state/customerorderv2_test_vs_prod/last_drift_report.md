# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-15T02:10:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1deb32c63430b77a437394ce3b9abaf8ee1aabb501ef5470c54cb72198bb2496`
- PROD hash: `2eea055fd90106235450ef928434633e1042b6b569ca2cad5a0cd0319836bff7`

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
