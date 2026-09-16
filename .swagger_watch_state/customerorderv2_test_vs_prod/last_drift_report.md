# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-16T20:29:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ed5d3e66ed747a4a7c13271b59c9cde97d22d42f3e4f3d58a7a21b09be5a8b60`
- PROD hash: `e4e5aa948bb84ab3246fcee5ad3f824f2ec67a2ad7b089b681aa34d4984ed0a0`

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
