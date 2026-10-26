# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-26T01:52:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cc98b5de5dfbfebe35e087a9a9b717f9f244b80d0c53cc78ebb473bd8b0c29fd`
- PROD hash: `ed9d4d4be27a552a8fa9a89f7084c6057a321bd14df4b1d80cd1447a52222d3c`

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
