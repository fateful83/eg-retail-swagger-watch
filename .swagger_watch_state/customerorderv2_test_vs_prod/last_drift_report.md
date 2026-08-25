# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-25T12:19:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `49aa93b7aca883f590cdb6dad0e7de34f0dc53ffd4f4409663de04baab9cf9c0`
- PROD hash: `b850b1d0ee9f38964ce4abc8301bb5e8eae83c407690babedbaecc76b7833f53`

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
