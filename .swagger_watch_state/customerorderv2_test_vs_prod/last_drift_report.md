# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-07T06:55:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3a866abf062fe23a9eccf81ae2acc48139a1d9f742c866fd79d33a8dfd2c5d7d`
- PROD hash: `65c70b98cb50ba0e27f9f3a2e4add9cf94c3df0f815a0d304843f49c188bce6d`

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
