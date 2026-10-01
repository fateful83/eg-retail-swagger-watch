# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-01T17:32:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a37d5588caae3632f66d49a6c5807ff70fec37cc042b8c0ca4175d875d346877`
- PROD hash: `f92927b463269207447176d7893c813cd643a64d1fb94fb68901765563d3247f`

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
