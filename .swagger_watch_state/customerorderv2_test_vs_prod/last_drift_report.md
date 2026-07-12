# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-12T01:16:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2bd81c9e7dbb2ebe173c1d9b786c3ed7666f2ee58b929464f463be38c98af1bd`
- PROD hash: `300d04f2898d3ca979200d1fd6e9754bf7c96114b26465ea11920159fead2667`

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
