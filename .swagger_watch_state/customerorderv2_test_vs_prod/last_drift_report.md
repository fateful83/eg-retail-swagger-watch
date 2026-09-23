# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-23T20:44:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d9903c388fed971d980b4157069a3e1de89e47047497c3805686991153ee0a6f`
- PROD hash: `6c4a7ff7f8fbff0a8348990735d689ba92f2192bca5c1b3842b03bcb7bf51146`

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
