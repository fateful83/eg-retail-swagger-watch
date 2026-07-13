# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-13T19:07:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a1a8b626f090d1b7f1648ef0253631daff95d9874455783708ab1fe6a11ef3ab`
- PROD hash: `516ab18b46a9323c9fbcccdd1696d1b0c59669191d889072e3447ed898c7e679`

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
