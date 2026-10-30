# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-30T03:02:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ff493afc3b38fb350e104ace185573d5aa7178dca1d87f1a2f5541d117df15d4`
- PROD hash: `b77c1fb1db76a597ddae0f4a5b8b1f2db5fb01f7fa910aa35d5a2150d32a150d`

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
