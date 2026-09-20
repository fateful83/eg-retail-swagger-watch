# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-20T10:09:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `42ca47e19485a6731d975ad9008ba2622faffcbc43c9e6bd4945745e1e07910a`
- PROD hash: `9c312342610ce847f146af2d2fcff55a7eb0adc1ceab5e18b7aea326a2e14e69`

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
