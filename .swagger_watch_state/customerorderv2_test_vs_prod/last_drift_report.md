# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-11T02:19:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eef9f581adb2d799dc28af1f60422a4f267579261651584316e30478d04605d8`
- PROD hash: `65c5b35d567ae9666d7ddab990edbfc8854b3dde0152c6e7da8828ae05007a5d`

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
