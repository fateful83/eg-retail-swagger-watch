# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-10T08:54:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `602737ad8ae12d3fbdcbec2bf2a793fbf944225ad6cb530ce03dad2d86d99d9b`
- PROD hash: `7db4f00e2dba54bc5c74c8ef75842ccb6e4270b4b79ed7acc5a839e9d48b3f2a`

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
