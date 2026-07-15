# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-15T01:04:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `06f85c4a4cc20902321ec0cbb4260329091a391ec4f5abea8801e25883e80d80`
- PROD hash: `8910c60e08f1829396ff9e49f3d5cb6ec04caed1ed1e9dadf26d4052eda9de7d`

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
