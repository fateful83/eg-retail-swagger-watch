# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-27T14:02:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bb33023998066dada492063b28c7724d9364c975073dbca689c701cc65f55191`
- PROD hash: `f0ff60e65d85002b7e57803bae1e18fc87448c0cb82721c962369e7b72cb5f56`

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
