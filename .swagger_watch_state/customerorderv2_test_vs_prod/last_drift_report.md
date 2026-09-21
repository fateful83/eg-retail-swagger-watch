# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-21T11:10:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `90bd12ce815fe438d46346675ee0be389f7a541f94f3111795628a767bfb03ca`
- PROD hash: `dfc62222696c4ba3347d04a4f74537053c5fd6604fe6e6b1faa9ee150b0247c4`

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
