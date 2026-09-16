# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-16T10:20:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1392924aef4c1842248c29f9e148f658b13c8bf2834f725ccf8df7c583f1d74c`
- PROD hash: `4974a2b60a72ebc631f79c63ace1fe580ec634252a0254823675a9007dcc186d`

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
