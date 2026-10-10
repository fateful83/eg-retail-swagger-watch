# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-10T20:45:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `52b1bc1478456e95df8997076b34344d429e09971dff93d7a5a9a38eaca7e9fe`
- PROD hash: `dc520153e7d96d8d3182674bf53f02348d3b1e42e3e362f82db6855ab3b27311`

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
