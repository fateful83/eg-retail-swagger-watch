# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-28T01:48:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ea394c505c0e0d4dd7143f57ae44b1295b5d7fc2a7c78389cadbbdff52f4c536`
- PROD hash: `49486289734ce73d51a25dc4344c6e5421c8fb0b4669d39288956a33534a379c`

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
