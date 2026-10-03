# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-03T15:16:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9ec74b971d46f60612ecebb7515d55894f165facfc6fd24687f704297cd5db1b`
- PROD hash: `179b6a6e7c282c8d62e71829c4a503f5be72aec6d6809434fe09ab05204c13c0`

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
