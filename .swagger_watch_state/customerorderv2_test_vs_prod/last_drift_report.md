# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-05T19:07:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b9e47109b43bdc3ae52fc5ef01191f04da4dea8403def503a08713c31f4d335b`
- PROD hash: `c2258c4343c4f904946e8a4035fa6f5574dd8ea27771eac548e3e968d6ad68fd`

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
