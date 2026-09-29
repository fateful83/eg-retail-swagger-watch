# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-29T21:33:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d4df6876d7071c26769e26b714b625753e63707d5a470eee7d538c0a86ff1892`
- PROD hash: `49c5010930fba6765975a88ef130dc19cce4b63d757383d5b7a513e4827415f3`

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
