# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-13T08:38:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d02ef0f770a8babdbe3a34f6d8248641f689bfdd33a8dcce7fb348f3c294a7dc`
- PROD hash: `7072310961409f35bcfe19ca8cc0620512ac15d79bfedcbfc872943d90de9b58`

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
