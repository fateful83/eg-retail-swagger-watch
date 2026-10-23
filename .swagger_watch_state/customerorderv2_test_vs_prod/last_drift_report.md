# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-23T20:41:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7023f26ebfce2e3d9e6e731c9df3c3b5108e8ad4313fceab079988b6b13a8d67`
- PROD hash: `b2778bef04a8f3d3987c5a2add9f93d9c5d7ffa3e28bd743a743d4b7f0e14958`

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
