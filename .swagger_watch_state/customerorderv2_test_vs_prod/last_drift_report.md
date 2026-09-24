# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-24T01:43:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ac4a5431386ef63b2db29ca9af3c6299f75b228308209b2a7d1c90fdb9a24898`
- PROD hash: `053e2a8a7459b804302999195deac419597c7fe48c82397e35dd9cd78b59632d`

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
