# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-07T01:54:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `77e273b437f539ea035ab18dfa2156e61a1b01782bd852d485537b7915ebd907`
- PROD hash: `3352600033a8cd037854fb1dfb882243dbe1e9de0ec0ca4c20a32108ffde34a7`

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
