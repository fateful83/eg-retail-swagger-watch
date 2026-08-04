# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-04T19:14:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1bc8dc2dfbb3b9011d6af30547c8853196ea1edbd826bf475a1eb825aef3e1cc`
- PROD hash: `3b8aeb21e84642a3aee99fd54c27fcda964b7b154d2de7d24081a1a74ee30ea8`

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
