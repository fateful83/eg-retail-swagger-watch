# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-29T02:00:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `35871d2618bb5ead76d0ddb2ea4108c3d970f45785bbaec4c7eff983c32c0cdb`
- PROD hash: `4bd6a76590c41009e5b92db40f3aab4f9bd2d641c7a22b178a80c2391a292ec1`

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
