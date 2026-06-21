# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-21T02:09:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8673c76559cbefdf202f31e565b9b022d4c1641648822c6502031a50fd0ceba0`
- PROD hash: `501afb05308ad2546621befeaf15340dcad11b0cab22d141823ef2ccd76fe694`

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
