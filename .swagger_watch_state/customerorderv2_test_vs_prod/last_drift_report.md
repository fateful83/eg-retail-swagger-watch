# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-20T08:36:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `65909c02b1b2fea2e4a3d0f25cc0d72c7fce830aeb609a819ca26ae8fa593fc6`
- PROD hash: `d48aa4142b0b005072795e16fcd27c6512892979baecea176f14d840f1ef42c3`

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
