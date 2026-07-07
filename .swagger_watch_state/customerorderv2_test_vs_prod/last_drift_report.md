# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-07T08:58:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `28df18d2ad9e5ec1c1fce0043caac56130c27b5b04157af0ff3ae2dd53125d69`
- PROD hash: `4d97d03c7177b96fb35ff73d7bc7b6a37bdbdf57a74627e8fd9d710151c48fac`

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
