# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-31T01:21:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `978c5fc1e3bcc24bbd48b973b302f29befb8ce030dec4e26d859e48f60cc168c`
- PROD hash: `308287ee1a7aa2a65412ae55e8d944709d9c1b744482f176c7b1a11d8eaafb40`

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
