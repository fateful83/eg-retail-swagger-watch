# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-19T14:52:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ad4aa5d0bb9c7ea61a6ea9907ddd1bd26c8e4aaee9fdf01948966d643e91e748`
- PROD hash: `89c5ccb3407f7b5fa8cd309973d85a70b018bae8fd652b10e97c7202f7cff8c6`

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
