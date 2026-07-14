# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-14T01:07:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `70b9794fbc5527664ccb9a05305d5328931f316ecf84ce63ac39462c7e0271c7`
- PROD hash: `86d255d966ca145d25ddc46edc021681f85e0c9f5084d9c8af0d72426703b06c`

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
