# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-16T07:49:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b6db0caf79c61d1e7081880477619273ce91431caa369417db80c0bb2e784c3d`
- PROD hash: `3ea580ed14871503a2d6a211812ecee629b0aa68ef32c841d37800b93ef4f4a8`

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
