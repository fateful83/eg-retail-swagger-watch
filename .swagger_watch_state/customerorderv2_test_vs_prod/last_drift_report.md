# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-03T08:41:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `efc1dec843562c2de41deb78a5abe0f16e850e2ee9cc14fef4dcd3db9d9e9d68`
- PROD hash: `2ffad8249c6c23e9f18a4456665067688188afe192ec2a6c1cda6783f1412fd2`

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
