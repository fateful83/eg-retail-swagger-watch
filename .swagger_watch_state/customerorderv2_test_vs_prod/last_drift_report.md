# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-23T08:52:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a0dac3fc6a8d72543c89449bec4602f6e55db01d64b395bef02a06796214f043`
- PROD hash: `87de583909f63f826067dea83c5f36bf16c9e1875c0da0354e2186ceecdd6e8a`

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
