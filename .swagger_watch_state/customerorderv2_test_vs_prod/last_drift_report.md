# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-24T00:26:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bce6646a4e57cb503f11ef01f6a0a9c1cdbec22bd303346153bf9de01a81bce2`
- PROD hash: `f9fd4a8986f234cb01a9c1e88d94d220712d5ff7e63f8d802a67617bc5233a79`

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
