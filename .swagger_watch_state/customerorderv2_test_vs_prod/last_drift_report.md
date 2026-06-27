# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-27T13:00:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e14c93862c429677bd141d1f981eb812479c21d586474069d3749e9933f61aa6`
- PROD hash: `9be01d7fdfb2ae289698713a84206f368b6913293b68e93645644e7f1b89d309`

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
