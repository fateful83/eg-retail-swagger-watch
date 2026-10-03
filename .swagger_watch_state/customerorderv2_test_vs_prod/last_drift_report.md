# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-03T02:25:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5b89a1caa81a11fa39c026931678f68f8938d3e4da0b70436967033ac2e437fa`
- PROD hash: `fb6f1e11fbafad0bc28ceccea137e6488d55defa18ad62d2db2ab4caf80121fa`

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
