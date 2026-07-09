# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-09T08:57:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3797f8d8be815cfbe7a64b63f2c361d855533159d2557424c7c95f89ab0b3b7d`
- PROD hash: `0eec3a584641624fe434d288f2c0c1b9e3065dc168cb0699e9726f3c7d7c435b`

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
