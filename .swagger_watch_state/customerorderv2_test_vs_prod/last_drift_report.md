# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-26T12:49:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `00236488c2bf9470478c342db33708e23c7c47c43ee43cf413b9de8560b1179c`
- PROD hash: `5baa6ab31c5b638d4d94218480b467f0b4a7ea4c941d958d644fcacd618a4082`

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
