# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-29T13:29:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `590cb53ffaccaf28bf0ab4448f17b705c5c928472078ffeb9d9a946d4c73afb5`
- PROD hash: `8003bb608936a3d3183657ff580df8437139d218653453cd1b2e08b2fc86d8db`

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
