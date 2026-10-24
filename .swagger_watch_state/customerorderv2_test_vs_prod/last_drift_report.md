# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-24T14:56:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `576e00fc4852b07b6801a6dae8be1b14f1630ea0a4e59f9935b84b878b234021`
- PROD hash: `c1fdbc1bb0e7180538577482536b5f1180bbe21db76d35ab94ac5d4cf2cfee3f`

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
