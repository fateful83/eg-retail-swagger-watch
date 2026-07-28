# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-28T08:07:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dc8ecde994236bc3a73f3e2d817216004186dd0eefb7842d7d95289394d96b32`
- PROD hash: `d08dce918237013efa6453ba896b5c5cd92a86fbf0f9c294f21e234b4153fbb1`

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
