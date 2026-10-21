# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-21T10:39:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `50782e3ebb9c18f7de389df9cbe4641d0ec0fd40a584e8105015638c5da2b0a7`
- PROD hash: `8fcee472cf59b0b3f41412d1bbdab17fce83c2e8f12b253ba393c20f06aa34d4`

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
