# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-17T07:47:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fc97d011e0370a978f190fe3d1c1d5ca01c9ca55c09caddf75f32b4831f920bf`
- PROD hash: `bfad2f8ebf9024fee6d87aa039ebfc52751a3c04b7d561bb482ebf8cb2e35d1a`

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
