# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-01T02:33:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0d09bd16b5344c18336f9f86316085282e675d4c22ed47c5ee2fea45ac0c7302`
- PROD hash: `82a823ba2123319dfdb67d4d1b4f86c5f3eb0c79cc6aa02171dffad9fad30f3a`

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
