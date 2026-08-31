# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-31T18:14:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2fba26671b986d8994d834f835e5cec16a432cbba9b30aa3f24f89a8ed5c9674`
- PROD hash: `e0dda93b344a03e3b434c85fa1267d495525eb6f9257b2a0dbad8e6edb88fcc5`

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
