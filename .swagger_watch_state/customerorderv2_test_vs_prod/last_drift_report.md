# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-21T06:21:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0e2825e002a5a578ec6231010d1d13636d855078934ee8d557dc763bcfd2525`
- PROD hash: `d9717160ba105ab59642e73cb06ffe395ef13d9e4af7d39b4b1faaedbab266dc`

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
