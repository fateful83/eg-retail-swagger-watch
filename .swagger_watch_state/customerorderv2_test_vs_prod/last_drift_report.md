# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-09T12:20:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2ac85f7040488015a755b834a9873fa00fd0cb9967d8fbcb6fc1e1a485350547`
- PROD hash: `2c5661edd8509ba31851566ffd9f547cf25c523b2d99b0b54fa8cee9122f6283`

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
