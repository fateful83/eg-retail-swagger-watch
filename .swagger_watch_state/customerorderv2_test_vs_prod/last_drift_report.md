# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-14T21:00:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `30ebe580cb61d9dc1ace6dbaaf8d802248a303444db463579815ab6d750d56c9`
- PROD hash: `cc2c422873430f4dc1cd0101a582cb07283954e7b9bd0874f5ecc2c67781a6d1`

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
