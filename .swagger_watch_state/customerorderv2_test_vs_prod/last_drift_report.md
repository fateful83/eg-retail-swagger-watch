# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-27T02:31:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a9a3eb3fc20c6aae7cd8e64fe3241da722a61930efe90651b5b6565b5814da7b`
- PROD hash: `398a64ab8dd3be6b867fe617e78de6dd12b2d90aa26cd82ab9e6000668b986a8`

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
