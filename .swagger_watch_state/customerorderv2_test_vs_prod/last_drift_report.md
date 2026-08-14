# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-14T00:47:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2ae5ec31ba07e81ce4efeeba4b5594bdfdf54fb6afc8c2806e3131745d2d4edc`
- PROD hash: `c4a6f6520712b9bfd5cfa877e2d6c39063e88b9d218755722ef4941ae6b7d888`

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
