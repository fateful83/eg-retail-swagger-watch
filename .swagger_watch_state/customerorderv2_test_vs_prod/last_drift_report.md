# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-18T01:37:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ff6558775afa72dc2d0be48bfd15ab4daa815fe01fd9885a6880670277996579`
- PROD hash: `4abd5f336bc2dba9be4dd171cc6d8b3cab171cc42005aa26f472517a0816f519`

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
