# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-12T01:51:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cc48726efde192475173924121e3984308d67a668a8c8b89096fb767be2db107`
- PROD hash: `2b07b104c39e3729239512833e9372140eb043aecbce4fb9d3d95bee71c41ab4`

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
