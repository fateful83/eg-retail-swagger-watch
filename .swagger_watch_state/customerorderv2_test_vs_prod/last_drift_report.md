# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-26T14:28:35Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `25d8d03e3fcb5e0280e873470c61f968f8b316b8d02ec3e71de502726c47d867`
- PROD hash: `e865a840991ea8eba98d46d6ce2a7d8300b4923476e07f8ff5f982655a34842f`

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
