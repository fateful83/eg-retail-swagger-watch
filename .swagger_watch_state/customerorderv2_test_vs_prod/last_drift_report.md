# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-01T11:53:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c98dc4e8056486896ee82cb4d90d3e93df668bf65793107fd62a5443e2276b04`
- PROD hash: `8a61ee968f3a2f400e347ba5dd70431884a484418554413f725acdab685f87e8`

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
