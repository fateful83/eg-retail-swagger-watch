# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-01T02:00:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0cad29c8e22764bde5f33782c1076202fd1c5dd20b2298d0a7668b3d38a22531`
- PROD hash: `a6b8dc5187ffd8fc3678df34e90e35926c3e548c3b5962984de80b5591ec6214`

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
