# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-31T13:04:41Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `70c74144acc14ccfa4628ba3769d38df7136cb47d5fb526008c40659681f07ad`
- PROD hash: `9f2d653f05e8afe0ea2513419ebd8c07b482f443646ae8eb17a81aec3dfe9b5d`

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
