# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-06T19:38:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b933a6a4e80e57ed8930e66c9a8d50971ab4b541b93986b54cf286732b48f26b`
- PROD hash: `0a86cea90e016605f5b7a960562452116c49543a6ab24856436a0c1adcf4c4d5`

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
