# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-22T01:58:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ed2a6c262a5e45570f723b71e2ad4853cbdaf9611b8ffbf5d57d5ca335dee018`
- PROD hash: `4906a2fd8c31c672be3adc11e05ea2f561ab3b221466ac6b9ce67a3264360d6d`

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
