# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-11T10:03:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3411465dc9815c5d0b236eb7708837d79e83a0c3f6a039162f8cfc338dc18113`
- PROD hash: `f79a0c84679b996384dfc0589c9bfd761fe725427cd2bec57b4a894e0354c1a8`

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
