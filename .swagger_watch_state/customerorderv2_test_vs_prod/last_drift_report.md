# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-18T19:43:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `79c040b8f1107175b07d4021d8d7c894a03cb7c8451e680e75f3e65d7cd6b2ed`
- PROD hash: `1382a9314465c7aa0eb152eb1dde4e343a943d6682a9504e9abeed6dfd96078f`

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
