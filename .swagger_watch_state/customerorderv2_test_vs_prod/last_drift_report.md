# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-28T19:00:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c50d9ca476a2c31cff5c47494171ebd5cd791283f62f5978d436eaaf35c39f81`
- PROD hash: `4346b0701debdce302aeaea8bd048cc8f6c6e4e814787d7a78326ce5cd9b4e33`

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
