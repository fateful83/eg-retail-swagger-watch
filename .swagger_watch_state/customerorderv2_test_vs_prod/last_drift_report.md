# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-19T02:35:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6bcfc4a1edb2bfdf473a316d63d9c46e7c3065503ef9f9849b6a68f94344477c`
- PROD hash: `98c2c4c30e407e22d0d4b3f9071783000d0961488ac16c07d7589d5ce4c35715`

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
