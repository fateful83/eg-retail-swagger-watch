# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-06T08:09:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `97921f2f911208a7c91becfa034c4b8b70ab10d3fc46525b74073386f2de732a`
- PROD hash: `7896328538e34a8a3b61d41b9b07df3aac557db80707a7f250ed2b17cd268de2`

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
