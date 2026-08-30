# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-30T10:45:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7246b7279e191ea16c3ea0d1698c0220695127aafcf8cdc72059c24662efc93b`
- PROD hash: `39edaae3def3552ca59083b2fe4484fdbb2ecde239ac09394395a26125454720`

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
