# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-23T08:04:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `68447f99b1b395305bdb45545e34c6c56ef3a02be81acd353d331c7dea750ded`
- PROD hash: `d368664fbdeebac65348ed9f5d58068e298ca8f4f83d15fa8d82527d307fb1df`

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
