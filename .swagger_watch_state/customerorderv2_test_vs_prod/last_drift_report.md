# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-14T02:06:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e7a44b6df94e321c40299b421b70d2842bf8c70d0e3b6bd5fccb5736f18ff7a3`
- PROD hash: `41dabc26ce6a43b12488361924a3f4ae27b5f319c8e82803f6029cd7a05ee665`

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
