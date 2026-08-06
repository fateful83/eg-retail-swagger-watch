# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-06T13:25:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3541c5ec2f61c462108f08321329691c48f30c66fdebf3103026bb79faefc8aa`
- PROD hash: `0c5f0aa10a80fad2f14081fceb16fa68542cc6cced6bd96435fc9aff5f4d1da9`

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
