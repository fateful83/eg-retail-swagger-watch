# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-09T03:12:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3f326f756e4376bcd5f01e2d33d8b63ce91974b1e3a8f115144eae4261330029`
- PROD hash: `e9291a7b24cd9ac4599b4d9fd4505ad741f50f43dd67cf858cb59b5048c9c77e`

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
