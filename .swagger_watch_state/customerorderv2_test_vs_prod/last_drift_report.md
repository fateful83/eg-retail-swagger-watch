# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-15T15:44:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `79472be9b3689fa4a041d6f799eea22fe301152b566e9a41d25124f6a102c793`
- PROD hash: `b6a423b27fe178519a84acaa29c6bb7e83115dec58c7b39181a1f4097e743810`

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
