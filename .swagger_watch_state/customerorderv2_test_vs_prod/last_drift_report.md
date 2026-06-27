# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-27T18:58:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7a880d5737c792eeeb9c330db3b6d6892f902e982a01689c40fd243e57b23a3e`
- PROD hash: `b23789e86ec34fd924cd5ee78d552d1caa22df84a79323e4c272e6524a6f601d`

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
