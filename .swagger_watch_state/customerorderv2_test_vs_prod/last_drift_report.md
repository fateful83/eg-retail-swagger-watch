# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-30T02:31:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e791af4e5c890f72c1048a69aca2944596c7e5c99947813ef77818632e9f203d`
- PROD hash: `707f16515f97cd0b5a4987823769ce475e4815bc364e1adac34e0e3814807763`

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
