# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-26T08:44:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7ce36fcf58b736c45fcdf9d026b947d0126c0ac9a50ef71c49c24de8e80e5a4a`
- PROD hash: `5a80cace422fa675c16214f8dd8de229b8df9fe6fe783ff97717a5718301daa5`

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
