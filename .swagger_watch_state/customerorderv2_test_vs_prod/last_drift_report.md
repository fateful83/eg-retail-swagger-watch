# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-30T12:55:32Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8a31596f895811addc069fcb2e9d3d3abffea53d7341a981cc688b55233f5f46`
- PROD hash: `e2facb92d36da0873d587384a0734307550e229cbc55fce088f5e96a20f0a636`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
