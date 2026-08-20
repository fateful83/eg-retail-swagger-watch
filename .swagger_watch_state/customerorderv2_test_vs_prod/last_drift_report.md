# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-20T06:21:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `478d0a24f9f5ae5da0b3b5997e8eb91645d6e6c277003fb3ea0aa02a8d57b2f5`
- PROD hash: `095034e8b6414a3b642e5897f130a5f9bb6e57cf1930bec2b20dd3759f950f0d`

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
