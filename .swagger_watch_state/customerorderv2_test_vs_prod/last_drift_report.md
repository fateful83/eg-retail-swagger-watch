# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-11T01:14:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d7fc2f54cdd2351147fe189da263d70e05fff9a98e0cf50bc7fea69684cfa9a1`
- PROD hash: `5c306909f7304cdcc4885d6845c61c1b51cdd2f571764230d4d94f60de4fa81c`

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
