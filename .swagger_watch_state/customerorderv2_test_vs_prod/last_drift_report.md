# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-11T18:39:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fbe3aa2b90c5ff963e73ff1acb506465cea746bb8d1756e005f77e9b69b432ca`
- PROD hash: `b511178be02a15a19b657eceb7cb13a05753c4f17b462e08e1ad5893a9190e09`

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
