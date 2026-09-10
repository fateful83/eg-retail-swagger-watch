# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-10T20:07:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1781854c9b591ed9b8949a710d8647f8e10d6199523361ad4bdbf485c177e410`
- PROD hash: `64702f9c472a5dda4c06d2a870df0e689ae7511da8219bb0476e85dee7d07951`

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
