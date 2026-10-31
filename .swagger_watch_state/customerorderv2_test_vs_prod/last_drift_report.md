# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-31T16:21:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `43f64f88de49967b3043433882167a2c51d46d41545a8524a8158725c9197bc3`
- PROD hash: `d521d1d12582ff7b03f768c35bd873b3d01fcc47237952cc2a917ee1e4bcdb4d`

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
