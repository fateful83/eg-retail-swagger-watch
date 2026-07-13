# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-13T01:17:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7eb02428678c49d09440e11b10c541c90b7668ad7b709ac45a8d0b056a0f20f2`
- PROD hash: `00e104ce0a15b417b55bdea80b8fcbbd9998d432ca17fa380b59cd76fee1c12a`

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
