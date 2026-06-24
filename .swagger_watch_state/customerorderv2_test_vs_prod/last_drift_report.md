# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-24T01:50:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ffe2f0287542f6cb9fbcce6bbf29429742a8ccb633465e2f542b2b8ebdbdb955`
- PROD hash: `ca6bafe05db509e579528979c0ad9082d77057887f9ab97531f3ac76fa22bd5f`

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
