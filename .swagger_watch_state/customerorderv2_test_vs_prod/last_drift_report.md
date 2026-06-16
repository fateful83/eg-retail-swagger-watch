# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-16T10:47:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d8cb7e01b39c0b6e9c030be2cfa49ba80056b23825bf916f2d9584ad0858c9f1`
- PROD hash: `179cb4b76b6bdbcc1c1c555c4b0783a2065bd28b144e04b7f10a5c55340c29bd`

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
