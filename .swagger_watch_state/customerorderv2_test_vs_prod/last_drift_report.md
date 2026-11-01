# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-01T02:42:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `67f51c911d611a6cebe9771dc5fb58a65d711d433fcc186651b134734e51cd80`
- PROD hash: `97e1bbd7f2e6fac395b6308c456a5572e230f6d85c28dc18a2b8d39d615ed4ea`

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
