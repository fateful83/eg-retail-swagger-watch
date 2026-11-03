# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-03T22:37:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a98c80fb3f7dd42086e316a6b8a1744021896b7f5700d527fcb721430464b529`
- PROD hash: `72d91d50c747f04b3cf95db2d9ba34ca25e7cf69d13e82658c06026bb4545738`

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
