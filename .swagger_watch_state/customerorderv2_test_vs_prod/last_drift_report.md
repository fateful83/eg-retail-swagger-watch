# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-23T01:20:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b9fe4381c2a48f0d4d2ad21b940150db6913866977508c00d4493d6b8cd8cd3c`
- PROD hash: `4a071542c7b80949e980768a85ddd2f33ab0aec3507ccd0bcca4b63e8638ce39`

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
