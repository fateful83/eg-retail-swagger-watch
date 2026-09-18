# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-18T20:02:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `20f8ee0d80aa607cf3ef0f38dbf2b1fb88aeb6eca309999984a6c8a3d5da3355`
- PROD hash: `d768a122f66dd3540fe63b323d6f237fe0aa05211105b2f20a1eab8496120fa4`

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
