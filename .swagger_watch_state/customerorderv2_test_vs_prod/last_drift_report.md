# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-01T12:06:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `536bb091c29a599922adda4370acd82fe01cb1b9dd00d336220cd6961d6ee732`
- PROD hash: `44ba5cab1b6abd4836cedff19a6485392646f5b134785efe6cb371096c0741d3`

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
