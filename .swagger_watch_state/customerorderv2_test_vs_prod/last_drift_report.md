# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-30T20:08:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `394b8714f326c8a69ec7781be6c685df5d5be2d9bd0e6b3bf791fe2fc3f1d3f1`
- PROD hash: `552fc9a66cbdc5dcc31313e5a87a6098fbb4f7f77156bc80098038ebc5207237`

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
