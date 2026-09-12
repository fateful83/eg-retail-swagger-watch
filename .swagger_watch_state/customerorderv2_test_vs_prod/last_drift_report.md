# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-12T14:25:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e766d969c0b2cff8d124c2fddac36bbea59177d76cf920e625c7373566c24b9`
- PROD hash: `0a0a3eb1d941bc5805228522d22a553828681e52012233a8da5a429df5f26527`

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
