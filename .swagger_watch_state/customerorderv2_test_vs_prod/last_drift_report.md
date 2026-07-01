# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-01T19:25:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `79b47d39d3b825dadae4bbb9c69eb8a7bdbcdc37d3990b1f27cb7d5d98ba21ed`
- PROD hash: `f93ac356fc50de525fb63e6f03a9d2dc9482df6d2e0dc783e6bfa8eefb17d735`

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
