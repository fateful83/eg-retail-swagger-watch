# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-15T20:30:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bc0079f139bdda898a9671bd5d8ead0ec334248a809cb9149ed2882d60686013`
- PROD hash: `c51ac34acb700addd7d407d74e50d9bbbfb1ea29e99a97d28b4e2ffeb9f45868`

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
