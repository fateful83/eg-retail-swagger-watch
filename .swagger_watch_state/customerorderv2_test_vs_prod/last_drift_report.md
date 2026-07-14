# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-14T07:30:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9be1983568809386a7039b77969f41304c20a7f878ccfe452c851fd0d848191d`
- PROD hash: `d04b3e483547384078123cb8776e021f60ea9918cbe7080ab2e200a72ab27e7d`

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
