# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-16T15:38:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `819697d6e5a38a7ae751ec08013c0da0c00d2cb3f05a4de1ca7c6da37d2bffab`
- PROD hash: `f828ce69528eacbe5e0c5d4b2d46e569cbc4b7a5e737b6aec571d6dbe98b97f2`

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
