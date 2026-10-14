# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-14T10:40:40Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `52bac5a23071bb4d0e8c12646bbc00818a6346b2896a50894e39b0d02b0a79f3`
- PROD hash: `ce0edf9c5316e0d20b391264f8ee2a9766d8edeccbbfeffb6903e4388372db76`

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
