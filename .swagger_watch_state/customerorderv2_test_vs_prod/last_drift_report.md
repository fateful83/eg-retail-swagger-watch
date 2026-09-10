# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-10T10:06:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `61275ec1889562fa7f4aa6aafca0ff29e6263cd3344f0895ac2064d0089a51a2`
- PROD hash: `d28e70e0f2b6b7fae6e1815ba69bd3935a1a8727623bd19ff4d77873a3f20463`

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
