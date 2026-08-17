# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-17T06:24:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9e6ca23dd2c8f8c832704f03e9251e649175c4efee6ec0e5c5aa9f5ffa4e81a2`
- PROD hash: `bda4870c48980da04142893eb263630874c269ac20faa5e2635d4b01b08d392b`

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
