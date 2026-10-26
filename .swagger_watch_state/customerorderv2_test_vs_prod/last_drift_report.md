# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-26T11:36:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cfc342222586f2ecee0bf3f745c0ad3f88954e5f53a9f981cc7ba75616c28cc8`
- PROD hash: `6cba84c923ac6af03488cc6d8af6da2267c8b2d0f137538824fd4a8f691e464a`

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
