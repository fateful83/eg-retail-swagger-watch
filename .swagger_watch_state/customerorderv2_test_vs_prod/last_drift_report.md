# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-22T11:25:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e8fcf58dbd1453514629771c548301c1a281b6635c253cf6ae9e41becac4337`
- PROD hash: `9f1ddc5c3ebf07712709456c13e8b134a06ba0c925a13e64bf53b08f0e8adb0c`

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
