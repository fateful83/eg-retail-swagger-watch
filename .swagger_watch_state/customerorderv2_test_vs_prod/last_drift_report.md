# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-20T13:18:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3e47894a52351269692771509dddd7b5251e1d189dcbc36caf675989959e4bd0`
- PROD hash: `7112a9fbc29fba5dfa6747f7bb38d2d636948f5e1bf606f2c588bb4a24fba6bb`

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
