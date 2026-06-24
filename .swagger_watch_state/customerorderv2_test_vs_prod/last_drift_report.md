# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-24T19:22:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b64b3a808d4c41870e260d9e18d774f31a149d7d2db2bd4f110e28ff63cc52a6`
- PROD hash: `9ddc8e7d168bdfdce608992c85422f647a2be28860cb9de05ab67b3771e9d111`

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
