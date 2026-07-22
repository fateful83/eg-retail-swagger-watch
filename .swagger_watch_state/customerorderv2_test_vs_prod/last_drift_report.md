# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-22T08:01:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3285485b04cb417d00a4299f14024bbe938f7c871fa8d10180706190c3c7aef3`
- PROD hash: `1186ccffb40bef901c505eed163c1a0c1cc071205db2ea9d6f38dc22fa07cd7e`

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
