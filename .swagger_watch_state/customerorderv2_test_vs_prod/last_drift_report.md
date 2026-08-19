# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-19T12:17:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a8af70dd2658b0b7e43f51c5540a323ea535344a99dfa27486067a3ed8f26f3c`
- PROD hash: `12a6d6a55d16ae3aa8d0596508bafb8f3969ed55d99914400c864634bcfba31a`

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
