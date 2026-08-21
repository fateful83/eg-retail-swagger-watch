# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-21T12:18:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8123f69c02c1b17073fe91f37b56ac07cd2c0eae6bdcd4a325c16a02b53e8ec5`
- PROD hash: `a848bd849974c96aed3ed47be13c4c8003f6c7bb49a238fe3f1f01f2cfc9db03`

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
