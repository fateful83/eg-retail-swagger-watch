# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-06T09:46:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0f28aef6721fd1c0ea34937aee641309ce0541c0372b3c31a7745c696148f137`
- PROD hash: `424a4243c5df7498e47b441ab32c6ec4315e179f96d3fef8292e69ac817a1516`

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
