# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-11T11:39:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5d016d63d01b92c11f17f6ccfd63b38a294c9716941db3a428a0b5053dfe6608`
- PROD hash: `be7bb6fa354c91732d51ad1c9a76cff294ed3a007e8eb9a44b8cf31e3b0d6ae5`

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
