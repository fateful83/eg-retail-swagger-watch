# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-16T15:36:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `74cc92a134bbf790c4ee7172ffa9f7057eecf3685b4f4ea99f4a33fd1e58e59c`
- PROD hash: `f4000e7cc18d0ed1069cc2caac75529cc1964c613970ad9c7117875511364d62`

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
