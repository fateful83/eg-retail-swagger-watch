# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-06T21:55:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `56f295d2b917146890fd69356e2af5ca134cf45fdf1aba6171c6fa9a43be9803`
- PROD hash: `b83d34f5ea6152f291d5d3494a4c5c8fdcde175cd0b245f8bcd5ae97d9673719`

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
