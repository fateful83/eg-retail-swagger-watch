# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-30T11:43:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `99ce50b58617ebb731a77aaad316d19295cd12b1a835f9bb16c525b679690c82`
- PROD hash: `670ec47e21335f7f598647705e5e0e15e913101db4d00d5fa724cad300790f86`

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
