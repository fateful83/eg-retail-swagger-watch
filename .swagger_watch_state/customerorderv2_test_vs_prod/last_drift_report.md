# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-30T01:48:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4ac3d485be77512eb580f936b5e985a56a3e60ff2908ddb9bd490b86fc7ae42f`
- PROD hash: `9ab1aa2bce270484256fc73f2377c6d62124e6aec94c396f0be39ebf2ddb1413`

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
