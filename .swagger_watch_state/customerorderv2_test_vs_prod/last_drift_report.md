# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-19T06:19:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1838f55c700aedb21710fca3fc49e83ac2aca4ef0a66938b260df7c20960cfd9`
- PROD hash: `d0ab7f3ab5b307abc66aa43690170129d1ef96422f759d5be3c0ece59fe83333`

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
