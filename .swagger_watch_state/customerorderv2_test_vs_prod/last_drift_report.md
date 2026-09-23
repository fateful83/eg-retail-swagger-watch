# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-23T15:36:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `484eac8865f3ccc392fa51feffc1ab4ffb61896d87ee9af4a01f41e0c0483501`
- PROD hash: `b17fd293d10b70f64bdb2767f3186929eb471f2d8c0a108022ba555d206b209e`

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
