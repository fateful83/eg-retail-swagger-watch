# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-31T20:43:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `97764b13fe5e5ca9aac5fefde6f45cff9247ca21361dcb5397c7c9f05e320e69`
- PROD hash: `ff18d18131fc631cb67bda6136879175eff0235367b3b357ca51f8ba0a88a2aa`

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
